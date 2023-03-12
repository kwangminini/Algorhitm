const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);

let result = 0;
arr.sort((a, b) => a - b);

for (let i = 0; i < n; i++) {
  result += arr[i] * (n - i);
}

console.log(result);
