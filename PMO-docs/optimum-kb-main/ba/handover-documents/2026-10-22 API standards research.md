# 2026-10-22 API standards research

Anton's research note for the BA, the TL and Mikhail. Written by Anton's agent
(claude-code/claude-opus-5-5) on 22 October. It is working material, not evidence (`ba/AGENTS.md`; moved from `pm/` on 29 October).
Nothing here is ingested, and no typed note changes.

We did not read the API documents themselves; they are sold per copy. What follows comes from
standards retailers, instrument manuals that quote the API procedures, AADE papers and one service
company's manual. Every formula should be checked against a purchased copy before it goes into code.
Our own conclusions are marked "evaluated". [[2026-10-21 MUDPRO research]] is the companion note on the
tool OES used before.

## Why we looked

- **Compliance.** On the introductory call of 20 October, Mr. Lawal said OES is "governed technically by
  API standards", and that "technical compliance to the American Petroleum Institute requirement ... an
  alignment in the way we design our tool is also paramount" (Bluedot recording
  6ad73c7c657f708925b041c5, not ingested, 45:35). The point was left out of the follow-up for the
  21 October internal meeting ([[2026-10-20 Introductory call follow-up]]).
- **Double-checking.** On the same call, OES offered "access to resources and data and equations",
  but added: "there needs to be a level of double-checking from your side in case if something is wrong
  or there's a mistake" (12:59). The API documents are the obvious independent reference for that.
- **What the SOW says.** SOW v10.4 puts the formulas and the compliance requirements on the client:
  - "deriving or validating the engineering formulas themselves is the Customer's responsibility"
  - "Security, data protection, certification, and compliance requirements (GDPR, ISO, local
    regulations) must be provided by the Customer before the project start"

  ([[2026-06-15 SOW v10.4 - rendering]] lines 339 and 451; [[COM-008 Client cooperation and
  dependencies]], [[CON-003 Correct calculations]]).

## What "API" means for drilling fluids

The API 13 series. Editions are as standards retailers list them (normservis, DIN Media, Accuris); API's
own catalogue page could not be reached. Its 2025 publications catalogue still shows RP 13D at the 7th
edition. The 13B-1 and 13D entries were checked on the retailer's page on 22 October.

| Document | Title | Current edition | What it governs | Weight for the app |
|---|---|---|---|---|
| Spec 13A | Drilling Fluids Materials | 19th, October 2019, two addenda and an errata to 2024 | Specifications for barite, hematite, bentonite, CMC, starch, PAC, xanthan and others | Low: the product list |
| RP 13B-1 | Testing Water-based Drilling Fluids | 6th, 1 January 2026, 144 pages; the 5th (2019) is withdrawn | Field tests on water-based mud | High |
| RP 13B-2 | Field Testing Nonaqueous-based Drilling Fluids | 6th, July 2023, 164 pages | Field tests on oil- and synthetic-based mud | High |
| RP 13C | Drilling Fluids Processing Systems Evaluation | 6th, December 2023 per an AADE paper; one catalogue still lists the 5th (2014) | Shakers, centrifuges, solids removal efficiency | Low |
| RP 13D | Rheology and Hydraulics of Oil-well Drilling Fluids | 8th, 1 April 2026, 137 pages; the 7th is September 2017, reaffirmed 2023 | Rheology models, pressure losses, ECD, bit hydraulics, hole cleaning, surge and swab | High |
| RP 13I | Laboratory Testing of Drilling Fluids | 9th, 2020, addendum 2023 | Laboratory, not rig, tests | Low |
| RP 13J | Testing of Heavy Brines | 6th, January 2023 | Completion brines | Low, unless OES does completions |
| RP 13K | Chemical Analysis of Barite | 4th, March 2022 | Laboratory analysis of barite | None |
| RP 13L | Training and Qualification of Drilling and Completion Fluids Specialists | 3rd, October 2024 | Competencies of fluids specialists | None |
| RP 13M | Measurement of Viscous Properties of Completion Fluids | 1st, 2004, reaffirmed | Completion fluids | None |
| RP 13G | Drilling Mud Report Form | Inactive (first published as RP 47 in 1969) | The old standard mud report form | See "The daily report" |

ISO counterparts:

- **ISO 10414-1** for RP 13B-1. It was identical to the 4th edition of 2009; the 5th and 6th are
  API-only.
- **ISO 10414-2** for RP 13B-2.
- **ISO 13500** for Spec 13A.
- **ISO 10416** for RP 13I.
- **None found for RP 13D.**

Two of the editions that matter most are very new: 13B-1 from January 2026 and 13D from April 2026. OES
may well work to older ones. We found no public list of what changed in either.

## The tests and their calculations (RP 13B-1 and 13B-2)

The tests, per the 13B-1 and 13B-2 scopes:

- **Water-based mud:**
  - density
  - viscosity and gel strength
  - static filtration, including HTHP and PPA
  - water, oil and solids
  - sand
  - methylene blue capacity
  - pH
  - alkalinity and lime
  - chloride
  - total hardness as calcium
  - low-gravity solids and weighting material
- **Nonaqueous mud:**
  - the same physical tests
  - whole-mud alkalinity, chloride and calcium
  - electrical stability
  - lime, CaCl2 and NaCl
  - solids

  Annexes cover activity, cuttings, sulfides and sag, among others.

The calculations, as the OFITE instruction manuals give them (they quote the API procedures), plus a
drilling manual site for the ion table. Units: lbf/100 ft2, cP, cm3, mg/L, lb/bbl.

```text
Rheology (direct-reading viscometer)
  PV (cP)             = θ600 - θ300
  YP (lbf/100 ft2)    = θ300 - PV
  AV (cP)             = θ600 / 2
  Gels 10 s, 10 min   = maximum dial reading after rest (30 min optional)

Filtration
  API filtrate        = volume after 30 min at 100 ± 5 psi, area 7.1 ± 0.1 in2
  HTHP filtrate       = 2 × V30 (500 psi differential, the cell has half the API area)
  PPA value           = 2 × V30
  Spurt loss          = 2 × (2 × V7.5 - V30)
  Static filtration rate = 2 × (V30 - V7.5) / 2.739

Retort and solids (densities g/cm3, MW lb/gal, Cs chloride mg/L)
  Vw  = 100 × water mL / sample mL
  Vo  = 100 × oil mL / sample mL
  Vs  = 100 - (Vo + Vw)
  Vss = Vs - Vw × [Cs / (1,680,000 - 1.21 × Cs)]
  Vlg = [100 × ρf + (ρb - ρf) × Vss - 12 × MW - (ρf - ρo) × Vo] / (ρb - ρlg)
  Vb  = Vss - Vlg
  Clg (lb/bbl) = 3.49 × ρlg × Vlg
  Cb  (lb/bbl) = 3.49 × ρb × Vb
  Defaults: ρlg 2.6, ρo 0.84, barite 4.2

Methylene blue
  MBC = mL methylene blue (0.01 meq/mL) / mL mud
  Bentonite equivalent (lb/bbl) = 5 × MBC

Alkalinity and lime (0.02 N H2SO4, endpoints pH 8.3 and 4.3)
  Lime (lb/bbl) = 0.26 × (Pm - Fw × Pf)        Fw = retort water as a fraction
  Lime (kg/m3)  = 0.742 × (Pm - Fw × Pf)
  OH-, CO3--, HCO3- (mg/L) from Pf and Mf, by case:
    Pf = 0      OH 0                  CO3 0                 HCO3 1220 × Mf
    2Pf < Mf    OH 0                  CO3 1200 × Pf         HCO3 1220 × (Mf - 2Pf)
    2Pf = Mf    OH 0                  CO3 1200 × Pf         HCO3 0
    2Pf > Mf    OH 340 × (2Pf - Mf)   CO3 1200 × (Mf - Pf)  HCO3 0
    Pf = Mf     OH 340 × Mf           CO3 0                 HCO3 0

Chloride (silver nitrate, after neutralising to pH 8.3)
  Cl (mg/L) = 1000 × mL AgNO3 (0.0282 N) / mL filtrate     below 10,000 mg/L
  Cl (mg/L) = 10,000 × mL AgNO3 (0.282 N) / mL filtrate    above 10,000 mg/L
  NaCl      = 1.65 × Cl

Hardness (EDTA)
  Total hardness as Ca (mg/L) = 400 × mL EDTA / mL filtrate

Nonaqueous mud (13B-2)
  POM  = (mL 0.1 N H2SO4 + base alkalinity demand) / mL mud
  Lime (lb/bbl) = 1.295 × POM
  Whole-mud Cl (mg/L) = 10,000 × mL 0.282 N AgNO3 / mL mud
  Whole-mud Ca (mg/L) = 4,000 × mL 0.1 M EDTA / mL mud
  Electrical stability: 340 ± 10 Hz, ramp 150 ± 10 V/s, test at 120 ± 5 °F or 150 °F,
    report the average of two readings within 5%
  Oil/water ratio = 100 × Vo / (Vo + Vw) : 100 × Vw / (Vo + Vw)
```

**Not confirmed:**

- The CaCl2, water-phase salinity, brine density and corrected-solids equations for nonaqueous mud. We
  could not open clause 12 or Annex E of 13B-2. Take them from the standard, not from us.

**Reading precision is part of the procedure.** A mud balance is read to 0.1 lb/gal (0.01 g/cm3 or
10 kg/m3), cake thickness to 1/32 in, filtrate to 0.1 cm3.

**The client's retort equations are these (evaluated).** Equations 10-2 to 10-8 in the client's samples
([[2025-11-20 Client formula and chart samples - rendering]] images 1 and 2) are the 13B-1 solids
analysis, term for term, with two differences to settle:

- **The concentration constant.** The client's sheet has 3.50, the OFITE manual 3.49.
- **The filtrate density.** The client's sheet has "ρ_f = 1 + 0.00000109 C_S". A secondary source gives
  1 + 1.94 × 10^-6 × Cl^0.95 instead (not confirmed).

## Rheology and hydraulics (RP 13D)

How the method changed:

- **1995 edition:** a dual power law. The pipe used θ600 and θ300, the annulus θ100 and θ3:
  - n_a = 0.657 log(θ100/θ3)
  - K_a = 5.11 θ100 / 170.2^n_a
- **2006 edition (5th), the major rewrite** (Zamora and Growcock, AADE-10-DF-HO-40; Hemphill 2017):
  - Herschel-Bulkley became the recommended model, with the "Unified" pressure-loss equations.
  - Yield stress is taken as the low-shear yield point, 2θ3 - θ6.
  - The bit nozzle coefficient went from 0.95 to 0.98.
  - Bingham plastic and the power law stay as special cases: yield stress = YP gives Bingham, yield
    stress = 0 gives the power law.
- **2010 and 2017:** no published change list found.
- **8th edition, April 2026:** what changed is unknown. Its scope says the equations are meant to be
  built in a common spreadsheet, and that the spreadsheet results are an order-of-magnitude
  determination, not the only valid answer.

The Herschel-Bulkley set, US oilfield units (AADE-05-NTCE-27, checked against the paper on 22 October;
AADE-10-DF-HO-40 ties it to RP 13D):

```text
Parameters from the 6-speed viscometer
  τy = 2θ3 - θ6                                (should not exceed YP)
  n  = 3.32 log10[(2PV + YP - τy) / (PV + YP - τy)]
  k  = (θ300 - τy) / 511^n
  np = 3.32 log10[(2PV + YP) / (PV + YP)]      (for the turbulent friction factor)
  shear rate (1/s) = 1.703 × rpm;  1.066 converts dial reading to lbf/100 ft2

Velocity (ft/min; Q gal/min; diameters in)
  pipe     V = 24.51 Q / d^2
  annulus  V = 24.51 Q / (dh^2 - dp^2)

Pressure loss, pipe (α = 0, dhyd = d) and annulus (α = 1, dhyd = dh - dp)
  G    = [((3 - α) n + 1) / ((4 - α) n)] × (1 + α/2)
  γw   = 1.6 G V / dhyd
  τw   = 1.066 [((4 - α)/(3 - α))^n τy + k γw^n]
  NReG = ρ V^2 / (19.36 τw)                    ρ in lb/gal
  laminar       f = 16 / NReG
  transitional  f = 16 NReG / (3470 - 1370 n)^2
  turbulent     f = a / NReG^b,  a = (log np + 3.93) / 50,  b = (1.75 - log np) / 7
  blended       fint = (ftrans^-8 + fturb^-8)^(-1/8);  f = (fint^12 + flam^12)^(1/12)
  ΔP (psi) = 1.076 ρ V^2 f L / (10^5 dhyd)
  critical Reynolds number = 3470 - 1370 n; critical velocity needs an iterative solve

ECD (lb/gal)
  ECD = MW + Σ ΔP annulus / (0.052 × TVD)
  downhole, MW should be the temperature- and pressure-corrected static density

Bit (TFA in2; Vn ft/s)
  ΔPbit = ρ Q^2 / (12,031 Cd^2 TFA^2)          Cd 0.95 gives the common 10,858 form
  TFA   = 0.000767 Σ J^2                        J = nozzle size in 32nds
  Vn    = 0.32086 Q / TFA
  HHP   = ΔPbit Q / 1714
  HSI   = 1.27 HHP / Dbit^2
  Impact force (lbf) = Vn Q ρ / 1930

Hole cleaning
  Cuttings transport ratio (%) = 100 (Va - Vslip) / Va
  Carrying capacity index = K × AV × MW / 400,000, with n and K from PV and YP; 1 or more is good

Surge and swab
  effective annular velocity = Va + Kc × Vpipe, clinging constant Kc about 0.45 (Burkhardt)
  EMW = MW ± ΔP / (0.052 × TVD)

Density under pressure and temperature (2006 and 2010 editions, per AADE-12-FTCE-44)
  per liquid phase  ρ(P,T) = (a1 + b1 P + c1 P^2) + (a2 + b2 P + c2 P^2) T
  phases combined by mass balance, solids incompressible
```

**The client's procedures are the older method (evaluated).** Figures 2-1 to 2-5 in the client's
samples (images 3 to 7) belong to the pre-2006 power-law family:

- n_a = 0.5 log(θ300/θ3) and n_p = 3.32 log(θ600/θ300).
- A Reynolds number with 928.
- Laminar friction 24/Re in the annulus and 16/Re in the pipe.
- A transition band from 3470 - 1370n to 4270 - 1370n.
- Pressure loss with 25.81, with velocities in ft/s.

The annulus pair θ300/θ3 is not the 1995 API pair (θ100/θ3) either. The client's program screen (image
8), by contrast, uses Herschel-Bulkley, which is current RP 13D. So "comply with API" and "use our
procedures" can give different numbers. That makes [[QUE-008 Which rheological model the hydraulics
must use]] sharper: it is a choice between the client's procedures and RP 13D, and which edition.

**Where common practice differs enough to move results** (from the research):

- **The model:** a single 600/300 power law, the 1995 dual set, Herschel-Bulkley, or the client's
  300/3 variant.
- **The laminar limit:** 2100, or 3470 - 1370n. In one manual example, an annulus at NRe 2,928.7 is
  turbulent by the first rule and laminar by the second: 16.66 psi against about 28.3 psi.
- **The bit constant.** One case (3 × 11/32 nozzles, 335 gal/min, 12.8 lb/gal) gives 1,707 psi with
  10,858, 1,604 psi with Cd 0.98, and 1,540 psi with no coefficient (our arithmetic).
- **Surface or downhole density** can outweigh any model difference.

**Cases with expected answers we can test against:**

- **A full worked example in a copy of the M-I SWACO Drilling Fluids Engineering Manual found online**
  (1995 method).
  - Inputs: 12.8 lb/gal, PV 19, YP 15, 335 gal/min.
  - Results: ECD 13.14 lb/gal, bit 1,700 psi, total 3,021.9 psi against 3,000 psi measured.
- **The carrying capacity index example** in AADE-04-DF-HO-42: PV 18 and YP 12 give 0.44 at 64.25
  ft/min and 12.3 lb/gal.
- **The client's own program screen** (image 8): one well at ten flow rates, inputs and outputs. Its
  Fann readings give PV 32 and YP 28, as the screen shows.
- **Whether RP 13D itself has worked examples:** to check in a purchased copy.

## The daily report

- **The old form standard is inactive.** API RP 13G, "Drilling Mud Report Form" (first published as RP
  47 in 1969), no longer appears in the catalogue.
- **The report form now sits in annexes** of the test standards: a water-based report form in 13B-1, an
  oil-based or "daily report form" annex in 13B-2. These are informative, not mandatory. We could not
  see their field lists.
- **WITSML Fluid is the nearest open field set** (Energistics), matching the test list above. It is the
  natural naming if data ever goes to other systems ([[REQ-019 API for other systems]]).
- **The vendor claim.** MUDPRO advertises a report that "meets the standards of API mud report format"
  ([[2026-10-21 MUDPRO research]]).

## Calibration

- **What 13B-1 and 13B-2 cover.** Both carry a calibration annex: glassware, thermometers, viscometers,
  the retort cup and mud balances, plus timers in 13B-1.
- **Viscometer.** The OFITE manual says 13B-1 and 13B-2 call for a monthly check:
  - certified fluid, read at 300 and 600 rpm
  - more than 1.5 dial units off fails
  - record the serial number, date and deviation
- **Other instruments:**
  - mud balance: checked with fresh water at 8.3 lb/gal
  - Marsh funnel: 946 mL of water runs out in 26 ± 0.5 s
  - electrical stability meter: checked against standards within 2%
- **Intervals.** No fixed API interval was found for anything but the viscometer. The rest would come
  from OES's own ISO 9001 procedures.

## How it affects the app

Our conclusions (evaluated):

1. **The mud check.** The 13B-1 and 13B-2 test lists decide the fields of a mud check, and they
   differ by mud type ([[CAP-004 Shift measurements and quality control]], [[TRM-008 Mud check]]). The
   client's Daily.xlsx already follows them closely.
2. **Derived values on save.** These are the 13B formulas above: mechanical, but each constant has to
   be settled, for example 3.49 against 3.50 ([[REQ-007 Derived values and standard calculations]]).
3. **Hydraulics and simulation: the largest effect.** RP 13D's Herschel-Bulkley set needs blended
   friction factors and an iterative solve for critical velocity, which is more work than the client's
   power-law procedures. The WBS shown to the client estimated "per 1 algorithm"
   ([[REQ-008 Fluid hydraulics simulation]], [[CON-003 Correct calculations]],
   [[QUE-008 Which rheological model the hydraulics must use]]).
4. **Correctness.** Each calculation should name its method, edition and constants, and be tested
   against a reference built from the cited equations and the worked examples above. The vendor tolerance
   noted for MUDPRO ("≤3% or ±0.3 ppg") is a fair end-to-end check. This is where losses would fall on us
   ([[K-2 Losses from a calculation defect fall on us]]).
5. **Units and precision.** API procedures fix the reading precision and are written in US oilfield
   units. The constants hold only in the units they were written for ([[REQ-018 Units of measure and
   conversion]], [[CAP-007 Units of measure]]).
6. **Entry checks** ([[REQ-005 Parameter thresholds and entry alerts]]). The standards don't set a
   well's acceptable ranges (the customer's mud programme does), but they give sanity rules:
   - readings fall with speed, θ600 ≥ θ300 ≥ ... ≥ θ3
   - yield stress not above YP
   - Vo + Vw not above 100
   - two electrical stability readings within 5%
7. **Records and traceability.** For ISO 9001, a stored result should carry the method and edition that
   produced it. That fits [[DEC-006 Calculations run in the desktop app, formulas fixed in the code]] and
   [[CAP-010 Audit trail and change approval]].
8. **Reports.** The 13B report-form annexes are a reference layout for the daily report
   ([[CAP-008 Reports and report approval]]).
9. **Calibration alerts.** An instrument register with due dates, the viscometer monthly, the rest by
   OES's procedures ([[REQ-016 Inventory of lab equipment and reagents]]).
10. **Products.** Spec 13A material types, and default densities (barite 4.2, hematite 5.0), for the
    product list ([[REQ-009 Inventory tracking]]).
11. **Access to the documents.** The API documents are copyrighted and sold per copy. The team needs
    copies to verify against; whether OES holds licensed copies it can share is open. Their text can't
    go into the app or our documents. Formulas and facts can.
12. **The contract.** "Comply with API" is open-ended on a fixed price, the growth [[K-5 Scope grows
    through the prototypes]] and [[K-10 Fixed price with vague acceptance criteria]] warn about. The SOW
    asks OES for the compliance requirements before the start and makes validating formulas theirs. Mr.
    Lawal's 12:59 remark expects us to double-check as well. That tension is for Mikhail and Aliaksandr
    Kavalchuk ([[COM-008 Client cooperation and dependencies]]).

## To ask OES

For the Discovery sessions; none of these blocks a WBS line yet, so they are not Question notes.
QUE-008 already asks the model question.

- Which API documents and editions OES works to (13B-1, 13B-2, 13D, 13C), and whether the team can have
  access to licensed copies.
- Where Figures 2-1 to 2-5 and Equations 10-2 to 10-8 come from, and whether they are the company
  standard or examples.
- For hydraulics: their procedures, RP 13D's Herschel-Bulkley, or both.
- Which tests are run on the rig for each mud type, including HTHP, electrical stability and activity
  for oil-based mud.
- Which report form is the reference: an API annex, the operator's (Aramco's), or their own Daily.xlsx.
- Calibration intervals per instrument under their ISO 9001 procedures.

## Sources

All read on 22 October 2026. Retailer and catalogue pages:

- [normservis, RP 13B-1 6th edition](https://eshop.normservis.sk/norma/apirp-13b-1-1.1.2026.html)
- [normservis, RP 13B-2 6th edition](https://eshop.normservis.sk/norma/apirp-13b-2-ed-6-1.7.2023.html)
- [normservis, RP 13D 8th edition](https://eshop.normservis.sk/norma/apirp-13d-1.4.2026.html)
- [Accuris, RP 13D 8th edition](https://store.accuristech.com/standards/api-rp-13d?product_id=3094668)
- [API 2025 publications catalogue](https://www.api.org/-/media/Files/Publications/2025-Catalog/2025_Pubs%20Catalog.pdf)
- [API, RP 13B-2 5th edition announcement](https://www.api.org/~/media/files/publications/whats%20new/13b-2%20e5%20pa.pdf)
- [API Monogram notice, Spec 13A 19th edition](https://www.api.org/-/media/Files/Certification/Monogram-APIQR/0_API-Monogram-APIQR/Advisories-Updates/Updates/API%20Specification%2013A%2019th%20Edition%20New%20Edition%20Update%2020191017.pdf)
- [normdocs catalogue, API 13 series](https://catalogue.normdocs.ru/standards/api/com.normdocs.dict.subject.record.api.subgroup_16787)
- [ISO 10414-1](https://www.iso.org/standard/41939.html)
- [GlobalSpec, API RP 13G](https://standards.globalspec.com/std/950255/API%20RP%2013G)

Test procedures:

- OFITE instruction manuals:
  - [viscometer](https://www.ofite.com/publications/instructions/5829-130-10-c-s-instructions/file)
  - [retort](https://www.ofite.com/publications/instructions/161-165-14-instructions/file)
  - [mud test kit](https://www.ofite.com/publications/instructions/145-144-95-instructions/file)
  - [methylene blue](https://www.ofite.com/publications/instructions/168-168-00-instructions/file)
  - [electrical stability](https://www.ofite.com/publications/instructions/131-131-50-instructions/file)
  - [mud balance](https://www.ofite.com/publications/instructions/5515-100-00-instructions/file)
- [Drilling Manual, Pf and Mf](https://www.drillingmanual.com/pf-mf-drilling-fluid-mud-alkalinity/)
- [Drilling Manual, oil-based mud tests](https://www.drillingmanual.com/oil-based-mud-testing-procedures/)
- [Energistics, WITSML Fluid](https://docs.energistics.org/WITSML/WITSML_TOPICS/WITSML-500-059-0-R-sv2000.html)

Rheology and hydraulics:

- [Zamora, Roy and Slater, AADE-05-NTCE-27](https://www.aade.org/application/files/1915/7304/0408/AADE-05-NTCE-27_Zamora.pdf)
- [Zamora and Growcock, AADE-10-DF-HO-40](https://www.aade.org/application/files/2315/7261/7998/AADE-10-DF-HO-40.pdf)
- [Zamora and Power, AADE-02-DFWM-HO-13](https://www.aade.org/download_file/2523/486)
- [Zamora et al., AADE-12-FTCE-44](https://www.aade.org/application/files/2115/7260/6803/AADE-12-FTCE-44_-_Zamora.pdf)
- [Robinson and Morgan, AADE-04-DF-HO-42](https://www.aade.org/application/files/5615/7295/4811/AADE-04-DF-HO-42.pdf)
- [Hemphill, SPE-GCS 2017](https://spegcs.org/files/12141)
- [AAPG Wiki, Wellsite math](http://wiki.aapg.org/Wellsite_math)
- [Drilling Manual, bit hydraulics](https://www.drillingmanual.com/drill-bit-pressure-drop-hydraulic-horsepower-impact-force-calculation/)
- [Drilling Manual, surge and swab](https://www.drillingmanual.com/surge-and-swab-pressure-calculations-drilling/)
- [a copy of the M-I SWACO Drilling Fluids Engineering Manual (third-party upload)](https://pdfcoffee.com/mi-swaco-2-pdf-free.html)
- [Amoco Drilling Fluids Manual (third-party upload)](https://oilfieldteam.com/static/uploads/uploaded_files/973f0f7560355125ebc95627ffe73527.pdf)

Project sources:

- the 20 October recording (not ingested)
- [[2025-11-20 Client formula and chart samples - rendering]]
- [[2025-10-29 Client sample daily report - rendering]]
- [[2026-06-15 SOW v10.4 - rendering]]
