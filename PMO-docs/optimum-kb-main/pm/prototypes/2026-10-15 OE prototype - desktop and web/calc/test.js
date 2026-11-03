const E = require('./engine.js');
const inp = {
  rho: 10.4, t600: 104, t300: 63, t6: 9, t3: 7,
  well: { md: 8450, tvd: 8120, shoeMd: 5271, shoeTvd: 5240,
    holes: [{ name: 'Casing 13 3/8', id: 12.347, top: 0, bottom: 5271 }, { name: 'Open hole', id: 12.25, top: 5271, bottom: 8450 }],
    string: [{ name: 'Drill pipe', od: 5.5, id: 4.67, len: null }, { name: 'HWDP', od: 5.5, id: 3.25, len: 496 }, { name: 'Jar', od: 6.75, id: 2.5, len: 33 }, { name: 'Drill collars', od: 8, id: 2.813, len: 270 }, { name: 'Bit', od: 12.25, id: 0, len: 1.4 }] },
  nozzles: [12, 12, 12, 12, 12, 12], bitSize: 12.25, surfE: 4.2e-5, cuttings: { d: 0.25, t: 0.1 }
};
// fix: the bit OD equals hole - exclude bit from annulus
inp.well.string = inp.well.string.filter((c) => c.name !== 'Bit').concat([]);
inp.well.string[0].len = null;
console.log('rheology', E.rheology(104, 63, 9, 7));
console.log('retort', E.retort(86, 0, 38000, 10.4));
for (const Q of [400, 500, 650, 750]) { const s = E.simulate(JSON.parse(JSON.stringify(inp)), Q); console.log(Q, Object.fromEntries(Object.entries(s).map(([k, v]) => [k, typeof v === 'number' ? +v.toFixed(2) : v]))); }
console.log('critical', E.critical(JSON.parse(JSON.stringify(inp))));
console.log('surge', E.surgeSwab(JSON.parse(JSON.stringify(inp)), 93, 60));
console.log('weightUp', E.weightUp(10.4, 11.0, 820, 4.2));
console.log('owr', E.oilWater(56, 24, 0.8, 820), E.oilWater(56, 24, 0.65, 820));
// Client sample check (image 8): OBM 77 lb/ft3 = 10.29 ppg, Fann 92/60/48/32/12/10, 6x12 nozzles, Type 4 surface, 650 gpm
console.log('client check surf@650', E.surfaceLoss(650, 10.29, 32).toFixed(1), 'jet', E.bitLoss(650, 10.29, [12,12,12,12,12,12], 12.25).jet.toFixed(1));
