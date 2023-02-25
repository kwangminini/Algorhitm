/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) return false;
  else {
    return x === reverse(x);
  }
};

function reverse(str) {
  const arr = str.toString().split("");
  const reverseArr = arr.reverse();
  return Number(reverseArr.join(""));
}
