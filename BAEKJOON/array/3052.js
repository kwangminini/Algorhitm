const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const remainder = [];
for (let i = 0; i < 10; i++) {
  remainder.push(Number(input[i]) % 42);
}

const result = remainder.reduce(
  (acc, cur) => (acc.includes(cur) ? acc : [...acc, cur]),
  []
);

console.log(result.length);
