---
type: source
kind: rendering
date: 2025-11-20
original: https://drive.google.com/drive/folders/1pC29fiMRRpXLm4ikHdjY4qJbZyH8TFKx
removed:
  - nothing; the images carry no money, personal data or credentials
  - not rendered - the ten thumbnails (file names with "-small-"), 256-pixel copies of the same ten images
---

# 2025-11-20 Client formula and chart samples - rendering

The ten images in the Drive folder "materials" that the client shared on 2025-11-20, transcribed on
2026-09-28 from the full-size PNG files. Each image is stored next to this rendering as "image 01" to
"image 10" and shown at the top of its section, for internal reference only (never in an export,
`procedures/ingest.md` step 2); the originals are in the Drive folder. Each section gives the Drive file
name as it is (the names look machine-made and are not titles; one shows a character-set error) and the
image's own heading. Never edited after storing.

How the formulas are written: each typeset formula is one line of plain text. `_` starts a subscript,
`^` a power, `sqrt()` is a square root, `log`, `×`, `÷` and `Σ` are as printed, minus signs are
written "-". Where the typesetting could be read two ways, the reading taken is said in square
brackets. A flowchart's boxes and connectors are given as a list of steps with their branches. The
charts in images 9 and 10 are described, not digitised: their axes, series and labels are
transcribed, the curves are not. Numbers are copied as shown; "[cut off]" marks text the image's edge
cuts.

## Image 1 - Equations 10-2 to 10-4

![[2025-11-20 Client formula and chart samples - image 01.png]]

File: "Equation 10-2_ Volume Percent Water-26.png",
https://drive.google.com/file/d/1SNmBt5nGyBokJeYNYlvcU3rXbPNY7ULu/view, 1149 x 498 px.

```text
Equation 10-2: Volume Percent Water
V_w = 100(volume of water, cm^3) / (volume of sample, cm^3)

Equation 10-3: Volume Percent Oil
V_o = 100(volume of oil, cm^3) / (volume of sample, cm^3)

Equation 10-4: Volume Percent Retort Solids
V_S = 100 - (V_W + V_O)
```

## Image 2 - Equations 10-5 to 10-8

![[2025-11-20 Client formula and chart samples - image 02.png]]

File: "100-108-918s-1214a-o-polval-34.png",
https://drive.google.com/file/d/1egvpaIjT70uCxj2AQyTQN52KrKQnpAs7/view, 1342 x 1942 px.

```text
Equation 10-5: Volume Percent Suspended Solids
V_ss = V_s - V_w (C_s / (1,680,000 - 1.21 C_s))

Where:
V_SS = Volume percent suspended solids
C_S = Chloride concentration (mg/L)

Equation 10-6: Volume Percent Low-Gravity Solids
V_lg = (1 / (ρ_b - ρ_lg)) [100 ρ_f + (ρ_b - ρ_f) V_SS - 12 W_m - (ρ_f - ρ_o) V_O]

Where:
V_lg = Volume percent low-gravity solids
W_m = Fluid weight (lb/gal)
ρ_f = Density of filtrate (g/cm^3); ρ_f = 1 + 0.00000109 C_S based on sodium chloride
ρ_b = Density of weighting material, g/cm^3; use 4.2 for barite and 5.0 for hematite
ρ_lg = Density of low-gravity solids (g/cm^3); use 2.6 if unknown
ρ_o = Density of oil (g/cm^3); use 0.84 if unknown

Equation 10-7: Volume Percent Weighting Material
V_b = V_SS - V_lg

Where:
V_b = Volume percent weighting material

Equation 10-8: Concentration of Low-Gravity Solids, Weighting Material, and Suspended Solids
C_lg = 3.50(ρ_lg)(V_lg)
C_b = 3.50(ρ_b)(V_b)
C_SS = C_lg + C_b

Where:
C_lg = Low-gravity solids concentration (lb/bbl)
```

The image ends after the first line of the last "Where:" list.

## Image 3 - Figure 2-1: Annular Pressure Drop and ECD

![[2025-11-20 Client formula and chart samples - image 03.png]]

File: "Figure 2-1_ Annular Pressure Drop and ECD-32.png",
https://drive.google.com/file/d/13u3cSiE-0YAoWhU4gOdCJy5dNzQxSLB6/view, 1338 x 1857 px.

```text
Figure 2-1: Annular Pressure Drop and ECD

Step 1    Draw Hole Geometry
Step 2    V_a = 0.408 (Q) / ((D_2)^2 - (D_1)^2)
Step 3.A  n_a = 0.5 log(θ_300 / θ_3)
Step 3.B  K_a = 5.11 (θ_300) / 511^(n_a)
Step 4    μ_ea = 100 K_a [144 V_a / (D_2 - D_1)]^(n_a - 1)
Step 5    Re_a = 928 V_a (D_2 - D_1) ρ / (μ_ea [(2 n_a + 1) / (3 n_a)]^(n_a))
Step 6.A  Re_L = 3470 - 1370 n_a
Step 6.B  Re_T = 4270 - 1370 n_a
Step 7    three branches:
          Laminar Flow       f_a = 24 / Re_a
          Transitional Flow  f_a = [(Re_a - Re_L) / 800] [((log n_a + 3.93) ÷ 50) / Re_T^(([1.75 - log n_a] ÷ 7)) - 24 / Re_L] + 24 / Re_L
          Turbulent Flow     f_a = ((log n_a + 3.93) ÷ 50) / Re_a^(([1.75 - log n_a] ÷ 7))
Step 8    P_a = ((f_a) V_a^2 (ρ) / (25.81 (D_2 - D_1))) (L)
Step 9    Repeat Steps 2 - 8 for each Annular Geometry
Step 10   P_aT = Σ P_a
Step 11   ECD = P_aT / ((0.052)(TVD)) + ρ
```

[In the transitional and turbulent boxes, "([1.75 - log n_a] ÷ 7)" is set above and after "Re_T" and
"Re_a", read here as their exponent. "511" in step 3.B carries "n_a" as its exponent.]

## Image 4 - Figure 2-2: Critical Velocity and Pump Rate

![[2025-11-20 Client formula and chart samples - image 04.png]]

File: "223010-D 61-28.png",
https://drive.google.com/file/d/1WrAqlHj8hP95yLlc2Px_Z6NlKc10yL7h/view, 1307 x 783 px.

```text
Figure 2-2: Critical Velocity and Pump Rate

Step 1    V_c = [ (Re_L K_a ((2 n_a + 1) / (3 n_a))^(n_a)) / (928 ρ (D_2 - D_1) [(144 / (D_2 - D_1))^(1 - n_a)]) ]^(1 / (2 - n_a))
Step 2    Repeat Step 1 for each Annular Geometry
Step 3    Compare each V_c to the corresponding interval V_a calculated from Figure 3-1. For each V_a that
          exceeds V_c, calculate Q_c for the interval
Step 4    Q_c = 2.45(V_c)(D_2^2 - D_1^2)
```

## Image 5 - Figure 2-3: Drillstring Pressure Drop

![[2025-11-20 Client formula and chart samples - image 05.png]]

File: "Figure 2-3_ Drillstring Pressure Drop-42.png",
https://drive.google.com/file/d/1kvaz4PHMT9zxFidAosJ4WJmvui0GLqFZ/view, 1321 x 1884 px.

```text
Figure 2-3: Drillstring Pressure Drop

Step 1    V_p = 0.408 Q / D^2
Step 2.A  n_p = 3.32 log(θ_600 / θ_300)
Step 2.B  K_p = 5.11 (θ_600) / 1022^(n_p)
Step 3    μ_ep = 100 K_p [96 V_p / D]^(n_p - 1)
Step 4    Re_p = 928 V_p (D_p) ρ / (μ_ep [(3 n_p + 1) / (4 n_p)]^(n_p))
Step 5.A  Re_L = 3470 - 1370 n_p
Step 5.B  Re_T = 4270 - 1370 n_p
Step 6    three branches:
          Laminar Flow       f_p = 16 / Re_p
          Transitional Flow  f_p = [(Re_p - Re_L) / 800] [((log n_p + 3.93) ÷ 50) / Re_T^(([1.75 - log n_p] ÷ 7)) - 16 / Re_L] + 16 / Re_L
          Turbulent Flow     f_p = ((log n_p + 3.93) ÷ 50) / Re_p^(([1.75 - log n_p] ÷ 7))
Step 7    P_p = ((f_p) V_p^2 (ρ) / (25.81 (D))) (L)
Step 8    Repeat Steps 1 - 7 for each different Pipe ID
Step 9    P_pT = Σ P_p
```

[The exponents in step 6 are read as in image 3.]

## Image 6 - Figure 2-4: Swab and Surge Pressures

![[2025-11-20 Client formula and chart samples - image 06.png]]

File: "Figure 2-4_ Swab and Surge Pressures-36.png",
https://drive.google.com/file/d/1QLA5Pj0wRvqW8Smf2n0NbN2DVbcV6Mx_/view, 1311 x 1936 px.

```text
Figure 2-4: Swab and Surge Pressures

Step 1    Method 1: V_pm = 60 L_s / t        Method 2: V_pm = 60 L_j / t
Step 2    V_m = [0.45 + D_1^2 / (D_2^2 - D_1^2)] V_pm
Step 3.A  n_a = 0.5 log(θ_300 / θ_3)
Step 3.B  K_a = 5.11 (θ_300) / 511^(n_a)
Step 4    μ_ea = 100 K_a [144 V_m / (D_2 - D_1)]^(n_a - 1)
Step 5    Re_a = 928 V_m (D_2 - D_1) ρ / (μ_ea [(2 n_a + 1) / (3 n_a)]^(n_a))
Step 6.A  Re_L = 3470 - 1370 n_a
Step 6.B  Re_T = 4270 - 1370 n_a
Step 7    three branches:
          Laminar Flow       f_a = 24 / Re_a
          Transitional Flow  f_a = [(Re_a - Re_L) / 800] [((log n_a + 3.93) ÷ 50) / Re_T^(([1.75 - log n_a] ÷ 7)) - 24 / Re_L] + 24 / Re_L
          Turbulent Flow     f_a = ((log n_a + 3.93) ÷ 50) / Re_a^(([1.75 - log n_a] ÷ 7))
Step 8    P_a = ((f_a) V_m^2 (ρ) / (25.81 (D_2 - D_1))) (L)
Step 9    Repeat Steps 2 - 8 for each Annular Geometry
Step 10   P_aT = Σ P_a
Step 11.A Surge Pressure EMW   EMW = P_aT / ((0.052)(TVD)) + ρ
Step 11.B Swab Pressure EMW    EMW = ρ - P_aT / ((0.052)(TVD))
```

[The exponents in step 7 are read as in image 3.]

## Image 7 - Figure 2-5: Slip Velocity and Hole Cleaning

![[2025-11-20 Client formula and chart samples - image 07.png]]

File: "ΓåÆ-Fieto-24.png" (as Drive lists it),
https://drive.google.com/file/d/10Aqj_LLQMmRD27OvlVpZcjXkPedzpDj1/view, 1223 x 1416 px.

```text
Figure 2-5: Slip Velocity and Hole Cleaning

Step 1    Determine the Interval Flow Regime
A  Laminar
   Step 2    γ_B = 186 / (D_c sqrt(ρ))
   Step 3    τ_p = 7.9 sqrt(T(20.8 - ρ))
   Step 4    γ_p = [τ_p / K_low]^(1 / n_low)
   Step 5    γ_p < γ_B  or  γ_p > γ_B
   Step 6    (γ_p < γ_B)  V_S = 1.22 × τ_p sqrt(γ_p × D_C / sqrt(ρ))
   Step 8    (γ_p > γ_B)  go to B-2
B  Turbulent
   B-1, Step 7   τ_p = 7.9 sqrt(T(20.8 - ρ))
   B-2           V_S = 16.62 × τ_p / sqrt(ρ)
Hole Cleaning (both branches join here)
   Step 9    NPT(ft/min) = V_A - V_S
             ITT(min) = Interval length ÷ (NPT)
   Step 10   ATT(min) = Σ ITT values
   Step 11   E_t = (NPT / V_a) × 100 = (1 - V_S / V_a) × 100
```

## Image 8 - Hydraulics summary, one well at ten flow rates

![[2025-11-20 Client formula and chart samples - image 08.png]]

File: "Dating luil-40.png",
https://drive.google.com/file/d/1MSKscVzgMxOPzEf7MEzrS90K6LKUNPQv/view, 1569 x 1220 px. A screenshot
of a program's output: tables only.

General

| Field | Value |
|---|---|
| Max Allw.SPP | 6000 psi |
| Surface Equipment | Type 4 |
| Bit Depth | 10000.00 |
| Bit TVD | 4221.85 ft |
| Bit Nozzles in/32 | 6x12 |
| TFA | 0.6627 in^2 |
| ROP | 50.0 ft/hr |
| RPM | 150 RPM |

Drilling Fluid

| Field | Value |
|---|---|
| Mud System | Oil Based |
| Mud Weight | 77.00 lb/ft^3 |
| PV \ YP | 32.00 cP \ 28.00 lbf/100ft^2 |
| Gel Strength, 10s\10min | 18 \ 12 lbf/100ft^2 |
| Rheological Model | Herschel-Bulkley |
| (model parameters) | K: 0.749[#sec^n/100ft^2] N: 0.689[-] YP: 9.000[lbf/100ft^2] |
| Fann 35 Speed | 600 \ 300 \ 200 \ 100 \ 6 \ 3 |
| Fann 35 Reading | 92 \ 60 \ 48 \ 32 \ 12 \ 10 |

Casing / Open Hole

| Type | OD in | ID in | Bottom MD ft |
|---|---|---|---|
| Casing | 13 3/8 | 12.347 | 5271.00 |
| Openhole | | 12 1/4 | 10000.00 |

Volumes bbl

| Field | Value | Field | Value |
|---|---|---|---|
| Annulus Volume | 1,162.810 | Hole Volume | 1,469.960 |
| String Displacement | 107.880 | String Volume | 199.270 |

Drill String

| Type | Length ft | OD in | ID in | TJ in \ in | Weight lb/ft |
|---|---|---|---|---|---|
| DP - WT56 / S-135 | 4534.05 | 5 1/2 | 4.670 | 7 1/4 \ 4 5/8 | 21.90 |
| HWDP - 5-1/2 FH / HW ... | 496.00 | 5 1/2 | 3 1/4 | 7 1/4 \ 3 5/16 | 61.63 |
| Jar | 33.49 | 6 3/4 | 2 1/2 | | 157.41 |
| HWDP - 5-1/2 FH / HW ... | 496.00 | 5 1/2 | 3 1/4 | 7 1/4 \ 3 5/16 | 61.63 |
| DP - WT56 / S-135 | 4278.00 | 5 1/2 | 4.670 | 7 1/4 \ 4 5/8 | 21.90 |
| HWDP - 5-1/2 FH / HW ... | 90.00 | 5 1/2 | 3 1/4 | 7 1/4 \ 3 5/16 | 61.63 |
| Sub - X/O | 3.00 | 8 | 2.813 | | 149.72 |
| HWDP - 6-5/8 FH / HW ... | 31.00 | 6 5/8 | 3 1/2 | 8 \ 4 1/2 | 71.43 |
| Sub - X/O | 2.00 | 8 1/4 | 3 | | 157.66 |
| Other | 24.70 | 8 1/4 | 5.109 | | 150.00 |
| Sub - X/O | 2.00 | 8 1/4 | 3 | | 157.66 |
| ATK - 9-1/2" ATK G3 ... | 8.31 | 9 | 6 3/4 | | 265.18 |
| Bit - PDC - fixed cu ... | 1.44 | 12 1/4 | | | 120.00 |

Bit Hydraulics and System Pressure Loss - W/ Cutting Effect, by flow rate

| Flowrate | USgal/min | 1050 | 950 | 850 | 750 | 650 | 550 | 450 | 350 | 250 | 150 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Bit Hydraulics** | | | | | | | | | | | |
| SPP | psi | 5224 | 4419 | 3691 | 3042 | 2483 | 2027 | 1705 | 1586 | 1899 | 3606 |
| Surface HP | HP | 3197.5 | 2447.3 | 1828.6 | 1329.9 | 940.7 | 649.9 | 447.3 | 323.6 | 276.8 | 315.3 |
| Bit Pressure Drop | psi | 2064 | 1690 | 1353 | 1053 | 791 | 566 | 379 | 229 | 117 | 42 |
| %SPP | % | 39.51 | 38.23 | 36.65 | 34.62 | 31.86 | 27.94 | 22.23 | 14.46 | 6.16 | 1.17 |
| Jet Velocity | ft/sec | 508.4 | 459.9 | 411.5 | 363.1 | 314.7 | 266.3 | 217.9 | 169.5 | 121.0 | 72.6 |
| Impact Force | lbf/in^2 | 24.1 | 19.8 | 15.8 | 12.3 | 9.3 | 6.6 | 4.4 | 2.7 | 1.4 | 0.5 |
| HSI | HP/in^2 | 10.88 | 8.05 | 5.77 | 3.96 | 2.58 | 1.56 | 0.86 | 0.40 | 0.15 | 0.03 |
| **System Pressure Loss - W/ Cutting Effect** | | | | | | | | | | | |
| Surf Equip | psi | 147 | 123 | 101 | 80 | 62 | 46 | 32 | 20 | 11 | 4 |
| DP, CSG, LNR, TBG | psi | 1680 | 1429 | 1194 | 975 | 775 | 592 | 429 | 288 | 189 | 152 |
| HWDP/CSDP | psi | 1032 | 877 | 731 | 596 | 473 | 360 | 260 | 173 | 101 | 45 |
| AutoTrak | psi | 37 | 30 | 24 | 19 | 14 | 10 | 7 | 4 | 2 | 1 |
| Additional Tools | psi | 112 | 95 | 79 | 64 | 51 | 39 | 28 | 19 | 11 | 5 |
| Annulus | psi | 152 | 176 | 209 | 253 | 317 | 413 | 570 | 853 | 1468 | 3357 |
| ECD w/ Cut- CSG Shoe | lb/ft^3 | 79.94 | 80.24 | 80.67 | 81.27 | 82.15 | 83.50 | 85.72 | 89.76 | 98.53 | 125.25 |
| ECD w/ Cut - BH | lb/ft^3 | 82.19 | 83.01 | 84.13 | 85.64 | 87.82 | 91.09 | 96.43 | 106.09 | 127.06 | 191.49 |

Below the last row, a further section heading [cut off]: only the top of its letters shows.

## Image 9 - Surge: depth against maximum trip speed, and the tripping-in table

![[2025-11-20 Client formula and chart samples - image 09.png]]

File: "2000-38.png",
https://drive.google.com/file/d/1o8oCXh1GvDOT59JJ3yi5L6LdW7GcMtR7/view, 1589 x 807 px. A screenshot of
a program's output: a chart on the left, a table on the right.

Chart "Surge: Depth Vs Maximum Trip Speed":

- Vertical axis "Depth [ft]", 0 at the top to 10000 at the bottom, gridlines every 1000.
- Horizontal axis "Max. Trip Speed [s/std]", 80 on the left falling to about 5 on the right, labels
  80, 70, 60, 50, 40, 30, 20, 10.
- Two filled areas, green and red, with no legend. The red area runs down the right edge (between
  about 10 and 5 s/std) from near the top to 10000 ft, and widens into a wedge that reaches 60 s/std at
  about 5200 ft, between about 3300 ft and 5900 ft. The rest is green.

Table "Tripping In Table" [the right edge cuts the last column after its first decimal]:

| Speed s/std | Float@5271.00 ft, P of I: Pressure psi | EMW lb/ft^3 | Float@10000.00 ft, TD: Pressure psi | EMW lb/ft^3 |
|---|---|---|---|---|
| 5.00 | 950 | 110.22 | 1005 | 112.1 [cut off] |
| 6.00 | 737 | 102.77 | 778 | 104.1 [cut off] |
| 7.00 | 600 | 97.98 | 632 | 99.0 [cut off] |
| 8.00 | 506 | 94.70 | 532 | 95.5 [cut off] |
| 9.00 | 439 | 92.34 | 460 | 93.0 [cut off] |
| 10.00 | 318 | 88.13 | 344 | 89.0 [cut off] |
| 12.00 | 299 | 87.44 | 322 | 88.2 [cut off] |
| 14.00 | 284 | 86.93 | 305 | 87.6 [cut off] |
| 16.00 | 272 | 86.52 | 292 | 87.2 [cut off] |
| 18.00 | 263 | 86.19 | 281 | 86.8 [cut off] |
| 20.00 | 255 | 85.92 | 273 | 86.5 [cut off] |
| 22.00 | 249 | 85.69 | 265 | 86.2 [cut off] |
| 24.00 | 243 | 85.50 | 259 | 86.0 [cut off] |
| 26.00 | 238 | 85.33 | 253 | 85.8 [cut off] |
| 28.00 | 234 | 85.17 | 249 | 85.6 [cut off] |
| 30.00 | 230 | 85.04 | 244 | 85.5 [cut off] |
| 32.00 | 227 | 84.92 | 240 | 85.4 [cut off] |
| 34.00 | 224 | 84.81 | 237 | 85.2 [cut off] |
| 36.00 | 221 | 84.72 | 234 | 85.1 [cut off] |
| 38.00 | 218 | 84.63 | 231 | 85.0 [cut off] |

The bottom edge cuts the 38.00 row through its middle; nothing below it shows.

## Image 10 - Inclination, hydraulics operating window and numerical data

![[2025-11-20 Client formula and chart samples - image 10.png]]

File: "Inclination-30.png",
https://drive.google.com/file/d/1yzeyTpKvvamH-SJ5Kz_EXZ_y1-CS60MJ/view, 1507 x 1089 px. A screenshot of
a program's output, three panels under the headings "Inclination deg", "Hydraulics Operating Window"
and "Numerical Data".

"Inclination deg":

- Vertical axis "Measured Depth [ft]", labels 0, 554, 1108, 1662, 2216, 2770, 3324, 3878, 4432, 4986,
  5540. Horizontal axis 0, 30, 60, 90 (degrees).
- A drawing of the well: an outer string labelled "CSG" to about 1108 ft, a second string with a
  label read as "LNR" to about 2900 ft, open hole below it to about 5300 ft, and the drill string inside,
  with the bottom-hole assembly drawn near the bottom. A small "0" sits near the bottom.
- A red curve, the inclination: 0 at the surface, building from about 700 ft to about 75 degrees at
  the bottom.

"Hydraulics Operating Window":

- Legend: SPP, ECD @ CS, ECD w/Cut @ CS, ECD @ Bit, ECD w/Cut @ Bit.
- Horizontal axis "Flowrate [USgal/min]", labels 600 to 1400 every 100. Left axis "Pressure [psi]",
  1000 to 6000. Right axis "ECD [lb/ft^3]", 78.5 to 84.5.
- A horizontal line "Max SPP" at 6000 psi, and an orange vertical band "Required Flowrate" near the
  right edge (about 1460 USgal/min).
- SPP rises from about 1100 psi at the left to about 4800 psi at the right. The two "w/Cut" ECD curves
  fall as the flow rate rises; the two ECD curves without cuttings rise slightly.

"Numerical Data":

Drilling Fluid: Mud System PERFORMAX; Mud Density 78.00 lb/ft^3.

| Field | Csg Shoe lb/ft^3 | Bottom lb/ft^3 |
|---|---|---|
| ECD /wo Cuttings | 78.76 | 79.02 |
| ECD w/ Cuttings | 79.34 | 79.73 |
| ESD /wo Cuttings initial | 78.00 | 78.00 |
| ESD w/ Cuttings initial | 78.31 | 78.31 |
| Pore Pressure | | 67.00 |
| Frac Pressure | 98.00 | |

Circulation Data

| Field | Value |
|---|---|
| Flowrate | 1470 USgal/min |
| ROP | 40.0 ft/hr |
| RPM | 150 RPM |
| Bit TFA | 1.8040 in^2 |

Flowrates

| Field | Value |
|---|---|
| Overall Req. | 1461 USgal/min |
| OH Required | 1384 USgal/min |
| OH Critical | 1866 USgal/min |

Below it the heading "System Pressure Loss" [cut off]: the bottom edge cuts the panel there.
