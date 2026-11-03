// OE prototype calculation engine - oilfield units.
// Sources: client samples (OES-BAR data sheet; Eq. 10-2..10-8; Figures 2-1..2-5).
// Assumptions (not in client samples): bit pressure drop 156*rho*Q^2/(sum dn^2)^2, surface equipment
// E*rho^0.8*Q^1.8*PV^0.2 (case 4, E=4.2e-5), oil/water ratio by mass balance, surge velocity converted ft/min -> ft/s.
const log10 = Math.log10;

function rheology(t600, t300, t6, t3) {
  const np = 3.32 * log10(t600 / t300);
  const Kp = 5.11 * t600 / Math.pow(1022, np);           // dyne*s^n/cm2
  const na = 0.5 * log10(t300 / t3);
  const Ka = 5.11 * t300 / Math.pow(511, na);
  const nLow = 3.32 * log10(t6 / t3);
  const KLow = t3 / Math.pow(5.11, nLow);                  // lbf*s^n/100ft2
  return { np, Kp, na, Ka, nLow, KLow, pv: t600 - t300, yp: 2 * t300 - t600 };
}

function retort(Vw, Vo, Cs, Wm, rhoB, rhoLg, rhoO) {
  rhoB = rhoB || 4.2; rhoLg = rhoLg || 2.6; rhoO = rhoO || 0.84;
  const Vs = 100 - (Vw + Vo);
  const Vss = Vs - Vw * (Cs / (1680000 - 1.21 * Cs));
  const rhoF = 1 + 0.00000109 * Cs;
  const Vlg = (1 / (rhoB - rhoLg)) * (100 * rhoF + (rhoB - rhoF) * Vss - 12 * Wm - (rhoF - rhoO) * Vo);
  const Vb = Vss - Vlg;
  const Clg = 3.5 * rhoLg * Vlg, Cb = 3.5 * rhoB * Vb;
  return { Vs, Vss, rhoF, Vlg, Vb, Clg, Cb, Css: Clg + Cb };
}

function friction(Re, n, lam) { // lam = 16 (pipe) or 24 (annulus)
  const ReL = 3470 - 1370 * n, ReT = 4270 - 1370 * n;
  const a = (log10(n) + 3.93) / 50, b = (1.75 - log10(n)) / 7;
  if (Re < ReL) return { f: lam / Re, regime: 'laminar' };
  if (Re > ReT) return { f: a / Math.pow(Re, b), regime: 'turbulent' };
  return { f: ((Re - ReL) / 800) * (a / Math.pow(ReT, b) - lam / ReL) + lam / ReL, regime: 'transitional' };
}

function pipeLoss(Q, D, L, rho, r) { // Figure 2-3
  const V = 0.408 * Q / (D * D);
  const mu = 100 * r.Kp * Math.pow(96 * V / D, r.np - 1);
  const Re = 928 * V * D * rho / (mu * Math.pow((3 * r.np + 1) / (4 * r.np), r.np));
  const fr = friction(Re, r.np, 16);
  return { V, Re, regime: fr.regime, P: fr.f * V * V * rho / (25.81 * D) * L };
}

function annLossV(V, D2, D1, L, rho, r) { // Figure 2-1 steps 4-8, V in ft/s
  const d = D2 - D1;
  const mu = 100 * r.Ka * Math.pow(144 * V / d, r.na - 1);
  const Re = 928 * V * d * rho / (mu * Math.pow((2 * r.na + 1) / (3 * r.na), r.na));
  const fr = friction(Re, r.na, 24);
  return { V, Re, regime: fr.regime, P: fr.f * V * V * rho / (25.81 * d) * L };
}

// Split the well into intervals: string components from the bit up, holes from the surface down.
function intervals(well) {
  const comps = well.string.slice(); // top -> bottom, last one fills to MD if length null
  let fixed = comps.reduce((s, c) => s + (c.len || 0), 0);
  comps.forEach((c) => { if (!c.len) c.len = well.md - fixed; });
  const out = []; let top = 0;
  comps.forEach((c) => {
    const bot = top + c.len;
    // split by hole sections
    let t = top;
    well.holes.forEach((h) => {
      const hTop = h.top, hBot = h.bottom;
      const a = Math.max(t, hTop), b = Math.min(bot, hBot);
      if (b > a) out.push({ comp: c.name, od: c.od, id: c.id, hole: h.name, holeId: h.id, top: a, bottom: b, len: b - a });
    });
    top = bot;
  });
  return out;
}

function bitLoss(Q, rho, nozzles32, bitSize) {
  const sum = nozzles32.reduce((s, d) => s + d * d, 0);
  const tfa = nozzles32.reduce((s, d) => s + Math.PI / 4 * Math.pow(d / 32, 2), 0);
  const P = 156 * rho * Q * Q / (sum * sum);
  const jet = 0.3208 * Q / tfa;
  const hhp = P * Q / 1714;
  const hsi = hhp / (Math.PI / 4 * bitSize * bitSize);
  return { P, tfa, jet, hhp, hsi };
}

function surfaceLoss(Q, rho, pv, E) { return (E || 4.2e-5) * Math.pow(rho, 0.8) * Math.pow(Q, 1.8) * Math.pow(pv, 0.2); }

function slip(Va_ftmin, rho, r, Dc, T) { // Figure 2-5, ft/min
  const gB = 186 / (Dc * Math.sqrt(rho));
  const tp = 7.9 * Math.sqrt(T * (20.8 - rho));
  const gp = Math.pow(tp / r.KLow, 1 / r.nLow);
  const Vs = gp < gB ? 1.22 * tp * Math.sqrt(gp * Dc / Math.sqrt(rho)) : 16.62 * tp / Math.sqrt(rho);
  return { Vs, eff: (1 - Vs / Va_ftmin) * 100, npt: Va_ftmin - Vs };
}

function simulate(inp, Q) {
  const r = rheology(inp.t600, inp.t300, inp.t6, inp.t3);
  const rho = inp.rho;
  const ivs = intervals(inp.well);
  // drill string: one pressure loss per component (by ID)
  let pString = 0;
  inp.well.string.forEach((c) => { if (c.id > 0 && c.name !== 'Bit') pString += pipeLoss(Q, c.id, c.len, rho, r).P; });
  let pAnn = 0, pAnnShoe = 0, minEff = 999, vaOH = null, vsMin = null;
  ivs.forEach((iv) => {
    const V = 0.408 * Q / (iv.holeId * iv.holeId - iv.od * iv.od);
    const a = annLossV(V, iv.holeId, iv.od, iv.len, rho, r);
    pAnn += a.P;
    if (iv.bottom <= inp.well.shoeMd + 1e-6) pAnnShoe += a.P;
    const s = slip(V * 60, rho, r, inp.cuttings.d, inp.cuttings.t);
    if (s.eff < minEff) { minEff = s.eff; vsMin = s.Vs; vaOH = V * 60; }
  });
  const bit = bitLoss(Q, rho, inp.nozzles, inp.bitSize);
  const pSurf = surfaceLoss(Q, rho, r.pv, inp.surfE);
  const spp = pSurf + pString + bit.P + pAnn;
  return {
    Q, spp, pSurf, pString, pBit: bit.P, pAnn, pctBit: bit.P / spp * 100, jet: bit.jet, hsi: bit.hsi, tfa: bit.tfa,
    ecdBit: pAnn / (0.052 * inp.well.tvd) + rho, ecdShoe: pAnnShoe / (0.052 * inp.well.shoeTvd) + rho,
    vaMin: vaOH, slip: vsMin, eff: minEff
  };
}

function critical(inp) { // Figure 2-2; x100 added to match the mu_ea definition of Figure 2-1 (missing in the transcribed figure)
  const r = rheology(inp.t600, inp.t300, inp.t6, inp.t3);
  const out = [];
  intervals(inp.well).forEach((iv) => {
    const d = iv.holeId - iv.od, ReL = 3470 - 1370 * r.na;
    const Vc = Math.pow((ReL * 100 * r.Ka * Math.pow((2 * r.na + 1) / (3 * r.na), r.na)) / (928 * inp.rho * d * Math.pow(144 / d, 1 - r.na)), 1 / (2 - r.na));
    out.push({ iv: iv.comp + ' / ' + iv.hole, Vc: Vc * 60, Qc: 2.45 * Vc * 60 * (iv.holeId * iv.holeId - iv.od * iv.od) / 60 });
  });
  return out;
}

function surgeSwab(inp, standLen, secPerStand) { // Figure 2-4, method 1, closed pipe clinging 0.45
  const r = rheology(inp.t600, inp.t300, inp.t6, inp.t3);
  const Vpm = 60 * standLen / secPerStand; // ft/min
  let P = 0;
  intervals(inp.well).forEach((iv) => {
    const Vm = (0.45 + iv.od * iv.od / (iv.holeId * iv.holeId - iv.od * iv.od)) * Vpm;
    P += annLossV(Vm / 60, iv.holeId, iv.od, iv.len, inp.rho, r).P;
  });
  return { Vpm, P, surge: inp.rho + P / (0.052 * inp.well.tvd), swab: inp.rho - P / (0.052 * inp.well.tvd) };
}

function weightUp(W1, W2, vol, sg, sackKg) {
  const per100 = 1472 * (W2 - W1) / (35.05 - W2);
  const sacks = per100 * vol / 100;
  const kg = sacks * (sackKg || 50);
  return { per100, sacks, tonnes: kg / 1000, volInc: kg / (sg * 1000) * 6.2898 };
}

function oilWater(Vo, Vw, targetOil, vol) { // targetOil as fraction, e.g. 0.8
  const cur = Vo / (Vo + Vw);
  if (targetOil >= cur) { const x = targetOil * Vw / (1 - targetOil) - Vo; return { cur, add: 'Base oil', bbl: x / 100 * vol, newVol: vol * (1 + x / 100) }; }
  const y = Vo / targetOil - Vo - Vw; return { cur, add: 'Water', bbl: y / 100 * vol, newVol: vol * (1 + y / 100) };
}

if (typeof module !== 'undefined') module.exports = { rheology, retort, simulate, critical, surgeSwab, weightUp, oilWater, intervals, bitLoss, surfaceLoss };
