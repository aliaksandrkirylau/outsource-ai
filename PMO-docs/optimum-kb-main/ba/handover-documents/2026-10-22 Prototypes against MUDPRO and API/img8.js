// Client program screen (image 8): Fann 92/60/48/32/12/10; screen shows HB K 0.749, n 0.689, YP(tau_y) 9.000
const L = Math.log10, r = { 600: 92, 300: 60, 200: 48, 100: 32, 6: 12, 3: 10 };
const PV = r[600] - r[300], YP = r[300] - PV, ty = 2 * r[3] - r[6];
const n = 3.32 * L((2 * PV + YP - ty) / (PV + YP - ty)), k = (r[300] - ty) / Math.pow(511, n);
console.log('RP 13D style: PV', PV, 'YP', YP, 'tau_y', ty, 'n', n.toFixed(3), 'k(dial)', k.toFixed(3), 'k x1.066', (k * 1.066).toFixed(3));
// tau_y fixed at the screen's 9: n, k from the same two-point formulas
const n9 = 3.32 * L((2 * PV + YP - 9) / (PV + YP - 9)), k9 = (r[300] - 9) / Math.pow(511, n9);
console.log('tau_y 9: n', n9.toFixed(3), 'k x1.066', (k9 * 1.066).toFixed(3));
// least-squares HB fit over the six readings (grid on tau_y, log-linear fit for n, k)
let best = null;
for (let t = 0; t < r[3]; t += 0.01) {
  const pts = Object.entries(r).map(([rpm, th]) => [Math.log(1.703 * rpm), Math.log(th - t)]);
  const m = pts.length, sx = pts.reduce((s, p) => s + p[0], 0), sy = pts.reduce((s, p) => s + p[1], 0);
  const sxx = pts.reduce((s, p) => s + p[0] * p[0], 0), sxy = pts.reduce((s, p) => s + p[0] * p[1], 0);
  const nn = (m * sxy - sx * sy) / (m * sxx - sx * sx), kk = Math.exp((sy - nn * sx) / m);
  const sse = Object.entries(r).reduce((s, [rpm, th]) => s + Math.pow(th - (t + kk * Math.pow(1.703 * rpm, nn)), 2), 0);
  if (!best || sse < best.sse) best = { t, nn, kk, sse };
}
console.log('fit: tau_y', best.t.toFixed(2), 'n', best.nn.toFixed(3), 'k x1.066', (best.kk * 1.066).toFixed(3));
