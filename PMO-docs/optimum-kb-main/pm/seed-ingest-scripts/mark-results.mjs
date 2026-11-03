// Fill the empty Result cell of every proposed-changes row: node mark-results.mjs <overview> <date> [rejected rows, comma-separated]
import fs from "node:fs";
const [file, date, rejected = ""] = process.argv.slice(2);
const rej = new Set(rejected.split(",").filter(Boolean));
const out = fs.readFileSync(file, "utf8").split("\n").map((l) => {
  const m = /^\| (\d+) \| ([^|]+) \|/.exec(l);
  if (!m || !/\|\s*\|\s*$/.test(l)) return l;
  const result = rej.has(m[1]) ? `rejected ${date}` : m[2].trim() === "no material" ? `recorded ${date}, no note` : `applied ${date}`;
  return l.replace(/\|\s*\|\s*$/, `| ${result} |`);
});
fs.writeFileSync(file, out.join("\n"));
console.log("rows marked:", out.filter((l) => new RegExp(`(applied|recorded|rejected) ${date}`).test(l)).length);
