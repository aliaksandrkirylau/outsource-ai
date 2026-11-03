#!/usr/bin/env perl
# kb-money - the money gate. Uses the rules in tools/money-patterns.txt, the same file kb-lint.mjs
# reads. Perl, because perl ships with Git for Windows and macOS and Node may not be installed.
#
#   perl tools/kb-money.pl --staged       the lines being added in the staged changes, content
#                                         areas only (kb-sync.sh and the pre-commit hook run this);
#                                         .js under pm/prototypes/ is skipped, the pages are not;
#                                         so is a sources/client/ rendering flagged
#                                         money: client-domain (both modes)
#   perl tools/kb-money.pl --files F...   whole files, any folder (screen a rendering before it
#                                         comes into the repo)
#   perl tools/kb-money.pl --samples      check the rules against tools/money-samples.txt
#
# Prints "MONEY <file>:<line> <rule>" for a figure tied to money and "MONEY? <file>:<line> <rule>"
# for one that may be. Exit 1 when any MONEY line is printed, 2 when it cannot run, 0 otherwise.
use strict;
use warnings;
use utf8;
use File::Basename qw(dirname);
binmode STDOUT, ':encoding(UTF-8)';
binmode STDERR, ':encoding(UTF-8)';

my $dir = dirname(__FILE__);
my (@err, @warn);
open my $pf, '<:encoding(UTF-8)', "$dir/money-patterns.txt" or do { print STDERR "kb-money: cannot read $dir/money-patterns.txt\n"; exit 2 };
while (my $l = <$pf>) {
  $l =~ s/\r?\n\z//;
  next if $l eq '' || $l =~ /^#/;
  my ($level, $name, $src) = split /\t/, $l, 3;
  my $re = eval { qr/$src/i };
  unless ($re && defined $src) { print STDERR "kb-money: bad rule '$name' in money-patterns.txt\n"; exit 2 }
  push @{ $level eq 'ERROR' ? \@err : \@warn }, [$name, $re];
}
close $pf;

my $content = qr{^(?:knowledge|sources|pm|ba|tl|qa|inbox)/|^log\.md\z};
# An exported prototype's runtime (support.js, vendor/React) is minified third-party code with no
# project text, and its "$1" strings trip the symbol rule. Its pages (.dc.html) are still screened.
# Approved by the curator, 2026-10-18 (log.md).
my $exempt = qr{^pm/prototypes/.*\.js\z}i;
# A client sample rendering the curator flagged `money: client-domain` keeps the client's own prices
# and costs, which the app computes (AGENTS.md rule 7). The flag counts only in the frontmatter of a
# rendering under sources/client/. Approved by the curator, 2026-11-02 (log.md).
my $client_domain = qr{(?:^|/)sources/client/[^/]+/[^/]+ - rendering(?: \d+)?\.md\z}i;
sub flagged {
  my $lines = shift;
  return 0 unless @$lines && $lines->[0][1] eq '---';
  for my $i (1 .. $#$lines) {
    my $l = $lines->[$i][1];
    return 0 if $l eq '---';
    return 1 if $l =~ /^money:\s*client-domain\s*\z/;
  }
  return 0;
}
# the staged version of a file, for the flag
my %staged_flag;
sub staged_flagged {
  my $file = shift;
  return 0 unless $file =~ $client_domain;
  return $staged_flag{$file} if exists $staged_flag{$file};
  my @b; my $n = 0;
  if (open my $h, '-|', 'git', '-c', 'core.quotepath=off', 'show', ":$file") {
    binmode $h, ':encoding(UTF-8)';
    while (my $l = <$h>) { $l =~ s/\r?\n\z//; push @b, [++$n, $l] }
    close $h;
  }
  return $staged_flag{$file} = flagged(\@b);
}

# Link targets, bare URLs, wikilinks and inline code without spaces (IDs) are not text.
sub blank {
  my $s = shift;
  $s =~ s/\]\([^)]*\)/]()/g;
  $s =~ s{https?://\S+}{ }g;
  $s =~ s/\[\[[^\]]*\]\]/ /g;
  $s =~ s/`[^`\s]*`/ /g;
  return $s;
}
sub first { my ($s, $rules) = @_; for my $r (@$rules) { return $r->[0] if $s =~ $r->[1] } return undef }

# screen(file, [ [line number, text], ... ] of consecutive lines) -> list of [level, file, line, rule]
sub screen {
  my ($file, $block) = @_;
  my @hits;
  my @t = map { blank($_->[1]) } @$block;
  for my $i (0 .. $#t) {
    my ($l, $next) = ($t[$i], $i < $#t ? $t[$i + 1] : undef);
    my $name = first($l, \@err);
    if (!defined $name && defined $next) {
      my $joined = first("$l $next", \@err);
      $name = $joined if defined $joined && !defined first($next, \@err);
    }
    if (defined $name) { push @hits, ['MONEY', $file, $block->[$i][0], $name]; next }
    my $w = first($l, \@warn);
    push @hits, ['MONEY?', $file, $block->[$i][0], $w] if defined $w;
  }
  return @hits;
}

sub read_lines {
  my $f = shift;
  open my $h, '<:encoding(UTF-8)', $f or do { print STDERR "kb-money: cannot read $f\n"; exit 2 };
  my @b; my $n = 0;
  while (my $l = <$h>) { $l =~ s/\r?\n\z//; push @b, [++$n, $l] }
  close $h;
  return \@b;
}

my $mode = shift @ARGV // '--staged';
my @hits;

if ($mode eq '--samples') {
  my ($group, $bad) = ('', 0);
  my @rows = @{ read_lines("$dir/money-samples.txt") };
  for my $k (0 .. $#rows) {
    my ($n, $l) = @{ $rows[$k] };
    if ($l =~ /^## (ERROR|WARN|PASS)/) { $group = $1; next }
    next if $l =~ /^#/ || $l eq '' || $group eq '' || $l =~ /^\.\.\. /;
    # a sample followed by a "... " line is screened together with it, as two lines
    my @block = ([$n, $l]);
    push @block, [$rows[$k + 1][0], substr($rows[$k + 1][1], 4)] if $k < $#rows && $rows[$k + 1][1] =~ /^\.\.\. /;
    my @h = grep { $_->[2] == $n } screen('money-samples.txt', \@block);
    my $got = !@h ? 'PASS' : $h[0][0] eq 'MONEY' ? 'ERROR' : 'WARN';
    if ($got ne $group) { $bad++; print "SAMPLE line $n should be $group, is $got: $l\n" }
  }
  print $bad ? "kb-money: $bad sample(s) misplaced\n" : "kb-money: all samples land where they should\n";
  exit($bad ? 1 : 0);
}
elsif ($mode eq '--files') {
  for my $f (@ARGV) {
    my $b = read_lines($f);
    (my $p = $f) =~ tr{\\}{/};
    if ($p =~ $client_domain && flagged($b)) { print STDERR "kb-money: $f skipped - money: client-domain\n"; next }
    push @hits, screen($f, $b);
  }
}
elsif ($mode eq '--staged') {
  open my $git, '-|', 'git', '-c', 'core.quotepath=off', 'diff', '--cached', '-U0', '--no-color', '--no-ext-diff', '--no-renames'
    or do { print STDERR "kb-money: cannot run git diff\n"; exit 2 };
  binmode $git, ':encoding(UTF-8)';
  my ($file, $ln, $header, @block) = ('', 0, 1);
  my $flush = sub { push @hits, screen($file, [@block]) if @block && $file =~ $content && $file !~ $exempt && !staged_flagged($file); @block = () };
  while (my $l = <$git>) {
    $l =~ s/\r?\n\z//;
    if ($l =~ /^diff --git /) { $flush->(); $header = 1; $file = ''; next }
    if ($header && $l =~ m{^\+\+\+ (?:b/(.*)|/dev/null)\z}) { ($file = $1 // '') =~ s/\t\z//; next }
    if ($l =~ /^@@ -\S+ \+(\d+)(?:,\d+)? @@/) { $flush->(); $header = 0; $ln = $1; next }
    next if $header;
    if ($l =~ /^\+(.*)\z/s) { push @block, [$ln++, $1]; next }
    $flush->();
  }
  $flush->();
  close $git;
}
else { print STDERR "usage: kb-money.pl [--staged | --files F... | --samples]\n"; exit 2 }

print "$_->[0] $_->[1]:$_->[2] $_->[3]\n" for @hits;
exit((grep { $_->[0] eq 'MONEY' } @hits) ? 1 : 0);
