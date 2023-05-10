//설탕 배달
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
let n = Number(input[0]);
let result = 0;

while (1) {
  if (n < 2) {
    if (n === 0) {
      break;
    } else {
      result = 0;
      break;
    }
  }
  if (n % 5 === 0) {
    result += parseInt(n / 5);
    break;
  }
  n -= 3;
  result += 1;
}

return result === 0 ? -1 : result;
