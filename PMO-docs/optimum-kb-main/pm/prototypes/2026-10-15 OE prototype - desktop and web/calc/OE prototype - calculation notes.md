# OE prototype - calculation notes

Status: prototype, not verified against the client's worked examples. Oilfield units only.
Code: `engine.js` (same formulas as in the Claude Design screens 2.2, 4.1, 4.2), run `node test.js`.

## Formulas from the client's material

| What | Source | Where in the prototype |
|---|---|---|
| Weight up: sacks of 50 kg OES-BAR / 100 bbl = 1472 (W2 - W1) / (35.05 - W2) | OES-BAR product data sheet (oes.com.sa) | 4.1 |
| Retort solids, suspended solids, low-gravity solids, barite, concentrations | Eq. 10-4 to 10-8 (client samples, image 1-2) | 2.2 live, 2.3 |
| Power law n, K (pipe 600/300, annulus 300/3) | Fig. 2-1, 2-3 | 2.2, 4.2 |
| Annular pressure loss and ECD | Fig. 2-1 | 4.2 |
| Critical velocity and flow rate | Fig. 2-2 | 4.2 hole cleaning |
| Drill string pressure loss | Fig. 2-3 | 4.2 |
| Surge and swab EMW | Fig. 2-4 (method 1, clinging 0.45) | 4.2 |
| Slip velocity, transport efficiency | Fig. 2-5 (low-shear n, K from 6/3 rpm) | 4.2 |

## Our assumptions (to confirm with the client)

1. Bit pressure drop = 156 rho Q^2 / (sum of nozzle sizes in 1/32 in, squared)^2; jet velocity 0.3208 Q / TFA;
   HSI = (dP Q / 1714) / bit area. Not in the samples (their "Figure 3-1" was not sent).
2. Surface equipment loss = E rho^0.8 Q^1.8 PV^0.2, E = 4.2e-5 (case 4). Matches their sample screen at
   650 gpm (62.7 vs 62 psi).
3. Fig. 2-2 as transcribed gives ~18 ft/min critical velocity; adding x100 (as in the mu_ea of Fig. 2-1)
   gives ~380 ft/min. Prototype uses x100. Ask the client which is right.
4. Surge/swab: the mud velocity of Fig. 2-4 step 2 is in ft/min; converted to ft/s for steps 4-8.
5. Oil/water ratio: volume balance on retort oil and water, adding only oil or only water. Not from the client.
6. ECD without cuttings effect; no temperature/pressure effects on mud; power law only (client's sample
   program uses Herschel-Bulkley - QUE-008).
7. Low-shear K for slip velocity in lbf*s^n/100ft2 (no 5.11 factor), n from 6/3 rpm.

## Test values (DW-217 mock well: 10.4 ppg, dial 104/63/49/34/9/7, 13 3/8 casing to 5,271 ft,
## 12 1/4 open hole to 8,450 ft MD / 8,120 ft TVD, 6 x 12 nozzles)

| Output | Value |
|---|---|
| n / K pipe | 0.72 / 0.69 lbf*s^n/100ft2 |
| Retort solids / LGS / barite | 14.0 % / 10.8 % (98 lb/bbl) / 1.2 % (18 lb/bbl) |
| At 650 gpm: SPP / bit dP / annulus / string / surface | 2,291 / 918 / 107 / 1,199 / 66 psi |
| At 650 gpm: ECD bit / shoe | 10.65 / 10.63 ppg |
| Jet velocity / HSI at 650 gpm | 315 ft/s / 2.95 HP/in2 (jet matches client sample 314.7) |
| Critical flow rate (lowest, collars in open hole) | 1,544 gpm |
| Slip velocity / transport efficiency at 650 gpm | 7.5 ft/min / 94 % |
| Surge / swab, 93 ft stand in 60 s | 10.58 / 10.22 ppg |
| Weight up 10.4 -> 11.0 ppg, 820 bbl | 302 sacks, 15.1 t, +22.5 bbl |
| OWR 56/24 -> 80/20, 820 bbl | add 328 bbl base oil |

## Ask the client for

Worked examples with expected results for each formula; the manual's name and edition and the missing
Figure 3-1; their hydraulics program's export for one well so the prototype can be compared line by line.
