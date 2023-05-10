const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
let [a, b] = input[0].split(" ").map(Number);

let count = 1;
while (1) {
  if (a === b) {
    console.log(count);
    break;
  }
  if (b.toString().at(-1) === "1") {
    count += 1;
    b = Number(b.toString().slice(0, -1));
  } else if (b % 2 === 0) {
    count += 1;
    b = parseInt(b / 2);
  } else {
    console.log(-1);
    break;
  }
}
