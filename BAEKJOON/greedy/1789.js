const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const n = Number(input[0]);
let count = 0;
let accNum = 0;

while (accNum <= n) {
  count += 1;
  accNum += count;
}
console.log(count - 1);
