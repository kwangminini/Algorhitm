// const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const n = 4;
const liter = [3, 3, 4];
const price = [1, 1, 1, 1];
// const n = Number(input[0]);
// const liter = input[1].split(" ").map(Number);
// const price = input[2].split(" ").map(Number);
let count = 0;
let selectPrice = price[0];
let result = 0;
for (let i = 0; i < price.length - 1; i++) {
  if (selectPrice >= price[i + 1]) {
    result += selectPrice * liter[i];
    selectPrice = price[i + 1];
  } else {
    result += selectPrice * liter[i];
  }
}

console.log(result);
