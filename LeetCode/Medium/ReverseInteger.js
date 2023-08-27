/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let result = 0;
  while (x != 0) {
    const remainNum = x % 10;
    result += remainNum;
    x = parseInt(x / 10);
    if (x != 0) {
      result = result * 10;
    }
  }
  return isRange(result);
};

function isRange(num) {
  if (num < -1 * 2 ** 31 || num > 2 ** 31 - 1) {
    return 0;
  }
  return num;
}
