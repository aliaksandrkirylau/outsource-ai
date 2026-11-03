#Requires -Version 5.1
<#
.SYNOPSIS
    Rehearse the PM Copilot install as if on a brand new machine, without touching
    anything of yours.

.DESCRIPTION
    Extracts a real .plugin into a throwaway folder and runs the installer out of it
    with the environment redirected, so every side effect lands in the scratch folder
    instead of your profile:

      USERPROFILE, APPDATA, LOCALAPPDATA  -> scratch
      UV_INSTALL_DIR, UV_TOOL_DIR, UV_TOOL_BIN_DIR, UV_PYTHON_INSTALL_DIR, UV_CACHE_DIR
      PATH                                -> stripped of Python and uv

    Stripping PATH is the point: the installer then cannot find uv or any Python and
    has to bootstrap from nothing, which is the path a real PM takes and the one you
    can never exercise on your own machine.

    What this DOES prove: uv downloads and runs from nothing; uv fetches its own
    CPython; all three servers install; each one actually imports; the compatibility
    pin fires when it is needed; a Claude config gets written from scratch and parses.

    What it CANNOT prove: that Claude Desktop then loads those servers, the double-click
    launcher, the Google consent screens, and anything macOS. Those need a real machine.

    Before and after, it fingerprints your REAL config, credentials and uv tools, and
    reports whether any of them moved. That check is the point of the whole script.

.PARAMETER Plugin
    Path to the .plugin file. Defaults to pm-copilot.plugin next to this script.

.PARAMETER Scratch
    Where to build the throwaway profile. Defaults to a folder in TEMP.

.PARAMETER Keep
    Leave the scratch folder behind for inspection. It is kept on failure regardless.

.EXAMPLE
    .\Test-CleanInstall.ps1
#>

[CmdletBinding()]
param(
    [string] $Plugin,
    [string] $Scratch,
    [switch] $Keep
)

$ErrorActionPreference = "Stop"

function Head { param($m) Write-Host "`n=== $m" -ForegroundColor Cyan }
function Ok   { param($m) Write-Host "  PASS  $m" -ForegroundColor Green }
function No   { param($m) Write-Host "  FAIL  $m" -ForegroundColor Red }
function Note { param($m) Write-Host "        $m" -ForegroundColor DarkGray }

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $Plugin)  { $Plugin  = Join-Path $here "pm-copilot.plugin" }
if (-not $Scratch) { $Scratch = Join-Path $env:TEMP ("pmc-cleantest-" + (Get-Date -Format "yyyyMMdd-HHmmss")) }

if (-not (Test-Path $Plugin)) { throw "No .plugin at $Plugin" }

Write-Host ""
Write-Host "  PM Copilot - clean-machine rehearsal" -ForegroundColor White
Write-Host "  Nothing outside the scratch folder is written to." -ForegroundColor DarkGray
Note "plugin  : $Plugin"
Note "scratch : $Scratch"

# ---------------------------------------------------------- fingerprint the real profile

# Taken BEFORE anything runs, compared after. This is what turns "it should be isolated"
# into "it was isolated".
function Fingerprint {
    $fp = [ordered]@{}
    $pkg = Get-ChildItem -Path (Join-Path $env:LOCALAPPDATA "Packages") -Directory -Filter "Claude_*" -ErrorAction SilentlyContinue | Select-Object -First 1
    $cfg = if ($pkg) { Join-Path $pkg.FullName "LocalCache\Roaming\Claude\claude_desktop_config.json" }
           else      { Join-Path $env:APPDATA "Claude\claude_desktop_config.json" }
    $fp["claude config path"] = $cfg
    $fp["claude config"]      = if (Test-Path $cfg) { (Get-FileHash $cfg -Algorithm SHA256).Hash } else { "(absent)" }
    $cred = Join-Path $env:USERPROFILE ".pm-copilot\google-oauth-client.json"
    $fp["credentials"]        = if (Test-Path $cred) { (Get-FileHash $cred -Algorithm SHA256).Hash } else { "(absent)" }
    try   { $fp["uv tools"]   = (& uv tool list 2>$null | Out-String).Trim() } catch { $fp["uv tools"] = "(uv not found)" }
    # The PERSISTENT user PATH, read from the registry rather than $env:PATH. An installer
    # that edits this leaves a change no amount of child-process env isolation prevents,
    # and the first version of this harness missed it entirely - so the run reported
    # "nothing of yours moved" while a TEMP folder sat at the front of the real PATH.
    $fp["user PATH (registry)"] = "$((Get-ItemProperty 'HKCU:\Environment' -Name Path -ErrorAction SilentlyContinue).Path)"
    $lb = Join-Path $env:USERPROFILE ".local\bin"
    $fp["local bin"]          = if (Test-Path $lb) { (Get-ChildItem $lb -File | ForEach-Object { "$($_.Name):$($_.Length)" }) -join "," } else { "(absent)" }
    return $fp
}

Head "Fingerprinting your real setup"
$before = Fingerprint
Note "claude config : $($before['claude config'].Substring(0, [Math]::Min(16, $before['claude config'].Length)))..."
Note "credentials   : $($before['credentials'].Substring(0, [Math]::Min(16, $before['credentials'].Length)))..."
Ok "captured"

if (Get-Process -Name "Claude" -ErrorAction SilentlyContinue) {
    Write-Host ""
    Write-Host "  Claude Desktop is running." -ForegroundColor Yellow
    Write-Host "  The rehearsal will run everything up to the settings write and stop there," -ForegroundColor Yellow
    Write-Host "  because the installer refuses to edit settings while Claude is open. That still" -ForegroundColor Yellow
    Write-Host "  covers the part you cannot otherwise test: bootstrapping from nothing." -ForegroundColor Yellow
    Write-Host "  Quit Claude first if you want the settings write exercised too." -ForegroundColor Yellow
    Write-Host ""
}

# ------------------------------------------------------------------ build the scratch

Head "Building a throwaway profile"
$null = New-Item -ItemType Directory -Force -Path $Scratch
$home2 = Join-Path $Scratch "profile"
$app2  = Join-Path $home2 "AppData\Roaming"
$loc2  = Join-Path $home2 "AppData\Local"
$ext   = Join-Path $Scratch "bundle"
foreach ($d in @($home2, $app2, $loc2, $ext)) { $null = New-Item -ItemType Directory -Force -Path $d }

# Extract exactly what a PM receives, and run out of the extraction.
$zip = Join-Path $Scratch "bundle.zip"
Copy-Item $Plugin $zip -Force      # Expand-Archive refuses any extension but .zip
Expand-Archive -LiteralPath $zip -DestinationPath $ext -Force
$installer = Join-Path $ext "scripts\setup\Install-PMCopilot.ps1"
if (-not (Test-Path $installer)) { throw "The bundle has no scripts\setup\Install-PMCopilot.ps1" }
Ok "extracted $((Get-ChildItem $ext -Recurse -File).Count) files"

$secretFile = Join-Path $ext "scripts\setup\client-secret.txt"
if (Test-Path $secretFile) {
    $line = (Get-Content $secretFile | Where-Object { $_.Trim() -and -not $_.Trim().StartsWith("#") } | Select-Object -First 1)
    if ($line -and $line.Trim() -ne "PASTE_THE_CLIENT_SECRET_HERE") { Ok "client secret present in the bundle" }
    else { No "client secret is still a placeholder - the PM would be prompted" }
} else { No "no client-secret.txt in the bundle" }

# --------------------------------------------------------------------- run it redirected

Head "Running the installer with the environment redirected"

# PATH is REPLACED with the Windows system minimum rather than filtered. Filtering was
# the first attempt and it leaked: a WinGet-installed uv sat in a directory none of the
# patterns matched, so the installer found it and the from-nothing path was never
# exercised at all. An allowlist cannot leak the way a denylist does.
$cleanPath = "C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0"

$envMap = @{
    USERPROFILE            = $home2
    APPDATA                = $app2
    LOCALAPPDATA           = $loc2
    UV_INSTALL_DIR         = (Join-Path $home2 ".local\bin")
    UV_TOOL_DIR            = (Join-Path $app2 "uv\tools")
    UV_TOOL_BIN_DIR        = (Join-Path $home2 ".local\bin")
    UV_PYTHON_INSTALL_DIR  = (Join-Path $app2 "uv\python")
    UV_CACHE_DIR           = (Join-Path $loc2 "uv\cache")
    # uv discovers interpreters through the registry and standard install locations, not
    # just PATH - so clearing PATH is not enough to hide your system Python. The first
    # run of this harness quietly built all three tools on your Python 3.12 while
    # claiming to simulate a machine with none. only-managed forces uv to use nothing but
    # interpreters it downloads itself, which is what a fresh laptop actually looks like.
    UV_PYTHON_PREFERENCE   = "only-managed"
    # uv's standalone installer appends its install directory to the PERSISTENT user PATH
    # in the registry. The first run of this harness did exactly that, putting a folder
    # under TEMP at the front of the real PATH - so `uv` on the machine resolved into a
    # scratch directory the harness then told the user to delete. Isolating env vars in a
    # child process does not isolate a registry write.
    UV_NO_MODIFY_PATH      = "1"
    PATH                   = $cleanPath
}
foreach ($k in ($envMap.Keys | Sort-Object)) { Note "$k = $($envMap[$k])" }

# -Auto ONLY when Claude is already closed. With Claude open, -Auto would close YOUR
# Claude Desktop, which is the opposite of not disturbing your setup. Without it the
# installer stops politely at the settings write, which is what the warning above said.
$autoArg = ""
if (-not (Get-Process -Name "Claude" -ErrorAction SilentlyContinue)) {
    $autoArg = " -Auto"
    Note "Claude is closed, so the full run including the settings write will be exercised"
} else {
    Note "Claude is open, so -Auto is deliberately NOT passed - your app will not be touched"
}

$sw = [Diagnostics.Stopwatch]::StartNew()
$assign = ($envMap.GetEnumerator() | ForEach-Object { '$env:' + $_.Key + ' = ' + "'" + $_.Value + "'" }) -join "; "
$cmd = "$assign; & '$installer'$autoArg"
$log = Join-Path $Scratch "install.log"
Write-Host ""
& powershell -NoProfile -ExecutionPolicy Bypass -Command $cmd 2>&1 |
    Tee-Object -FilePath $log |
    ForEach-Object { Write-Host "    $_" -ForegroundColor DarkGray }
$sw.Stop()
Write-Host ""
Note "elapsed $([math]::Round($sw.Elapsed.TotalSeconds,1))s, log at $log"

# ------------------------------------------------------------------------ what happened

Head "Did the from-nothing path work"
$out = Get-Content $log -Raw

$uvExe = Join-Path $home2 ".local\bin\uv.exe"
if (Test-Path $uvExe) { Ok "uv bootstrapped into the scratch profile" }
elseif ($out -match "uv ready") { Ok "uv ready (check the log for where it came from)" }
else { No "uv never became available" }

$pyDir = Join-Path $app2 "uv\python"
# Filter to cpython-* - uv leaves a .temp staging folder in there, and reporting that as
# the interpreter version reads like a pass while proving nothing.
$managed = @(Get-ChildItem $pyDir -Directory -ErrorAction SilentlyContinue | Where-Object { $_.Name -like "cpython-*" })
if ($managed.Count -gt 0) {
    Ok "uv fetched its own Python: $(($managed | ForEach-Object { $_.Name }) -join ', ')"
} else { No "no managed Python was downloaded - check whether the network allowed it" }

# The real proof is which interpreter each tool got built on. If any of these point at a
# directory outside the scratch profile, the isolation leaked and the run proved nothing.
foreach ($pkg in @("workspace-mcp", "mcp-google-sheets", "notebooklm-mcp-cli")) {
    $tp = Join-Path $app2 "uv\tools\$pkg\Scripts\python.exe"
    if (-not (Test-Path $tp)) { continue }
    $bp = (& $tp -c "import sys;print(sys.base_prefix)" 2>&1 | Out-String).Trim()
    if ($bp -like "$Scratch*") { Ok "$pkg built on a scratch interpreter" }
    else { No "$pkg built on an interpreter OUTSIDE the scratch: $bp (isolation leaked)" }
}

foreach ($t in @("workspace-mcp", "mcp-google-sheets", "notebooklm-mcp")) {
    $exe = Join-Path $home2 ".local\bin\$t.exe"
    if (Test-Path $exe) { Ok "installed: $t" } else { No "missing: $t" }
}

if ($out -match "applying a compatibility pin") { Ok "the mcp-google-sheets pin fired, as expected today" }
elseif ($out -match "google-sheets installed") { Note "the pin did not fire - upstream may have shipped a fix, worth checking" }

# The import check the installer itself runs, repeated here independently.
$chk = Join-Path $Scratch "importcheck.py"
@(
 'import importlib, importlib.metadata as md, sys'
 'try:'
 '    eps = md.distribution(sys.argv[1]).entry_points'
 'except Exception as exc:'
 '    print("SKIP %s" % exc); raise SystemExit(0)'
 'mods = sorted({ep.module.split(":")[0] for ep in eps if ep.group == "console_scripts"})'
 'for m in mods:'
 '    importlib.import_module(m)'
 'print("IMPORT-OK")'
) | Set-Content $chk -Encoding ASCII

foreach ($pkg in @("workspace-mcp", "mcp-google-sheets", "notebooklm-mcp-cli")) {
    $tp = Join-Path $app2 "uv\tools\$pkg\Scripts\python.exe"
    if (-not (Test-Path $tp)) { Note "no tool env for $pkg, skipping import check"; continue }
    $r = (& $tp $chk $pkg 2>&1 | Out-String)
    if ($r -match "IMPORT-OK") { Ok "imports cleanly: $pkg" }
    elseif ($r -match "SKIP")  { Note "could not check $pkg" }
    else {
        No "DOES NOT IMPORT: $pkg"
        Note (($r -split "`n" | Where-Object { $_ -match "Error" } | Select-Object -Last 1))
    }
}

Head "The config it would give a PM"
$cfg2 = Join-Path $app2 "Claude\claude_desktop_config.json"
if (Test-Path $cfg2) {
    try {
        $j = Get-Content $cfg2 -Raw | ConvertFrom-Json
        Ok "written and parses as JSON"
        foreach ($n in $j.mcpServers.PSObject.Properties.Name) {
            $c = $j.mcpServers.$n.command
            $exists = (Test-Path $c)
            if ($exists) { Ok "  $n -> command exists" } else { No "  $n -> command NOT found: $c" }
        }
        $b = [System.IO.File]::ReadAllBytes($cfg2)
        if ($b.Length -ge 3 -and $b[0] -eq 0xEF -and $b[1] -eq 0xBB -and $b[2] -eq 0xBF) { No "has a BOM, which breaks Claude" }
        else { Ok "no byte-order mark" }
    } catch { No "written but is not valid JSON: $($_.Exception.Message)" }
} elseif ($out -match "Claude Desktop is still running") {
    Note "not reached - Claude was open, so the installer stopped before the settings write"
    Note "quit Claude and re-run this to exercise that part"
} else { No "no config was written" }

$cred2 = Join-Path $home2 ".pm-copilot\google-oauth-client.json"
if (Test-Path $cred2) {
    $cj = Get-Content $cred2 -Raw | ConvertFrom-Json
    $s = "$($cj.installed.client_secret)"
    if ($s -and $s -ne "<dry-run-placeholder>") { Ok "credentials written, secret length $($s.Length)" }
    else { No "credentials written but the secret is a placeholder" }
}

# ------------------------------------------------------------------------ safety proof

Head "Did any of YOUR setup move"
$after = Fingerprint
$moved = @()
foreach ($k in $before.Keys) {
    if ($k -eq "claude config path") { continue }
    if ($before[$k] -ne $after[$k]) { $moved += $k }
}
if ($moved.Count -eq 0) {
    Ok "your Claude config, credentials, uv tools and .local\bin are all byte-identical"
} else {
    foreach ($m in $moved) { No "CHANGED: $m" }
    Write-Host "        Your real Claude config is backed up next to itself if the installer touched it." -ForegroundColor Yellow
}

Head "Done"
Note "This did NOT test: Claude loading the servers, the double-click launcher,"
Note "the Google consent screens, or anything macOS. Those need a real machine."
if ($Keep -or $moved.Count -gt 0) {
    Note "scratch kept at $Scratch"
} else {
    Write-Host "        Remove the scratch folder with:" -ForegroundColor DarkGray
    Write-Host "          Remove-Item -Recurse -Force '$Scratch'" -ForegroundColor DarkGray
}
Write-Host ""
