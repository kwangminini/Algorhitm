const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const arr = input[0].split("-");
let result = 0;
for (let i = 0; i < arr.length; i++) {
  const number = arr[i]
    .split("+")
    .map(Number)
    .reduce((acc, cur) => acc + cur);
  if (i == 0) result += number;
  else result -= number;
}
console.log(result);
