// Compare the OE prototype engine (client power law, Fig. 2-1..2-5) with the RP 13D Herschel-Bulkley
// "unified" set as written in ba/handover-documents/2026-10-22 API standards research.md. Illustration only, not verified
// against RP 13D. Run: node hb-compare.js (optionally the path to engine.js as the first argument).
const path = require('path');
const E = require(process.argv[2] || path.join(__dirname, '../prototypes/2026-10-15 OE prototype - desktop and web/calc/engine.js'));
const log10 = Math.log10;
const inp = {
  rho: 10.4, t600: 104, t300: 63, t6: 9, t3: 7,
  well: { md: 8450, tvd: 8120, shoeMd: 5271, shoeTvd: 5240,
    holes: [{ name: 'Casing', id: 12.347, top: 0, bottom: 5271 }, { name: 'Open hole', id: 12.25, top: 5271, bottom: 8450 }],
    string: [{ name: 'Drill pipe', od: 5.5, id: 4.67, len: null }, { name: 'HWDP', od: 5.5, id: 3.25, len: 496 }, { name: 'Jar', od: 6.75, id: 2.5, len: 33 }, { name: 'Drill collars', od: 8, id: 2.813, len: 270 }] },
  nozzles: [12, 12, 12, 12, 12, 12], bitSize: 12.25, surfE: 4.2e-5, cuttings: { d: 0.25, t: 0.1 }
};
const clone = () => JSON.parse(JSON.stringify(inp));
// HB parameters
const PV = inp.t600 - inp.t300, YP = inp.t300 - PV, ty = 2 * inp.t3 - inp.t6;
const n = 3.32 * log10((2 * PV + YP - ty) / (PV + YP - ty));
const k = (inp.t300 - ty) / Math.pow(511, n);
const np = 3.32 * log10((2 * PV + YP) / (PV + YP));
function hbLoss(Q, dOut, dIn, L, rho, annulus) {
  const a = annulus ? 1 : 0, dh = annulus ? dOut - dIn : dOut;
  const V = annulus ? 24.51 * Q / (dOut * dOut - dIn * dIn) : 24.51 * Q / (dOut * dOut);
  const G = (((3 - a) * n + 1) / ((4 - a) * n)) * (1 + a / 2);
  const gw = 1.6 * G * V / dh;
  const tw = 1.066 * (Math.pow((4 - a) / (3 - a), n) * ty + k * Math.pow(gw, n));
  const Re = rho * V * V / (19.36 * tw);
  const flam = 16 / Re, ftr = 16 * Re / Math.pow(3470 - 1370 * n, 2);
  const A = (log10(np) + 3.93) / 50, B = (1.75 - log10(np)) / 7, fturb = A / Math.pow(Re, B);
  const fint = Math.pow(Math.pow(ftr, -8) + Math.pow(fturb, -8), -1 / 8);
  const f = Math.pow(Math.pow(fint, 12) + Math.pow(flam, 12), 1 / 12);
  return { V, Re, P: 1.076 * rho * V * V * f * L / (1e5 * dh) };
}
function hbSim(Q) {
  const w = clone().well; const ivs = E.intervals(w);
  let pStr = 0; w.string.forEach((c) => { pStr += hbLoss(Q, c.id, 0, c.len, inp.rho, false).P; });
  let pAnn = 0, pShoe = 0;
  ivs.forEach((iv) => { const r = hbLoss(Q, iv.holeId, iv.od, iv.len, inp.rho, true); pAnn += r.P; if (iv.bottom <= w.shoeMd + 1e-6) pShoe += r.P; });
  const tfa = inp.nozzles.reduce((s, d) => s + Math.PI / 4 * Math.pow(d / 32, 2), 0);
  const bit98 = inp.rho * Q * Q / (12031 * 0.98 * 0.98 * tfa * tfa);
  return { pStr, pAnn, ecdBit: inp.rho + pAnn / (0.052 * w.tvd), ecdShoe: inp.rho + pShoe / (0.052 * w.shoeTvd), bit98 };
}
console.log('HB: tauy', ty, 'n', n.toFixed(3), 'k', k.toFixed(3), 'np', np.toFixed(3), '| prototype PL: np', E.rheology(104,63,9,7).np.toFixed(3), 'na', E.rheology(104,63,9,7).na.toFixed(3));
console.log('Q    | proto string  HB string | proto annulus  HB annulus | proto ECDbit  HB ECDbit | proto bit(156)  bit Cd0.98');
for (const Q of [400, 500, 650, 750]) {
  const p = E.simulate(clone(), Q), h = hbSim(Q);
  console.log(Q, '|', p.pString.toFixed(0).padStart(6), h.pStr.toFixed(0).padStart(9), '|', p.pAnn.toFixed(0).padStart(8), h.pAnn.toFixed(0).padStart(11), '|', p.ecdBit.toFixed(2).padStart(8), h.ecdBit.toFixed(2).padStart(9), '|', p.pBit.toFixed(0).padStart(8), h.bit98.toFixed(0).padStart(11));
}
// Weight-up: 1472 = 42 gal/bbl x 35.05 ppg, so the result is lb barite per bbl (= 100-lb sacks per 100 bbl)
const lbPerBbl = 1472 * (11.0 - 10.4) / (35.05 - 11.0), lbTotal = lbPerBbl * 820, kg = lbTotal * 0.45359;
console.log('weight-up 10.4->11.0, 820 bbl: prototype', E.weightUp(10.4, 11.0, 820, 4.2).sacks.toFixed(0), 'sacks of 50 kg;', 'as lb/bbl:', lbPerBbl.toFixed(2), 'lb/bbl ->', (kg / 50).toFixed(0), 'sacks of 50 kg,', (kg / 1000).toFixed(1), 't');
// Retort constant 3.5 vs 3.49
const r = E.retort(86, 0, 38000, 10.4);
console.log('LGS lb/bbl 3.5:', r.Clg.toFixed(2), '3.49:', (3.49 * 2.6 * r.Vlg).toFixed(2), '| barite 3.5:', r.Cb.toFixed(2), '3.49:', (3.49 * 4.2 * r.Vb).toFixed(2));
// Excess lime from the v0 example fill (Pm 1.4, Pf 0.7, water 84%)
console.log('v0 example excess lime = 0.26 x (1.4 - 0.84 x 0.7) =', (0.26 * (1.4 - 0.84 * 0.7)).toFixed(2), 'lb/bbl; OE example (Pm 1.2, Pf 0.6, water 86%):', (0.26 * (1.2 - 0.86 * 0.6)).toFixed(2), 'lb/bbl, typed 0.3');
