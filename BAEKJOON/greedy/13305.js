const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const n = Number(input[0]);
const liter = input[1].split(" ").map(Number);
const price = input[2].split(" ").map(Number);

let minPrice = price[0];
let result = BigInt(0);
for (let i = 0; i < n - 1; i++) {
  minPrice = Math.min(minPrice, price[i]);
  result += BigInt(minPrice) * BigInt(liter[i]);
}

console.log(String(result));
