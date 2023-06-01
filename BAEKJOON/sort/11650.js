const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const arr = [];
for (let i = 1; i <= n; i++) {
  let [x, y] = input[i].split(" ").map(Number);
  arr.push([x, y]);
}
arr.sort(compare);
let result = "";
for (let [x, y] of arr) {
  result += x + " " + y + "\n";
}
console.log(result);

function compare(a, b) {
  if (a[0] != b[0]) return a[0] - b[0];
  else return a[1] - b[1];
}
