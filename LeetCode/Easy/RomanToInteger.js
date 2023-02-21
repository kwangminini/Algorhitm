/**
 * @param {string} s
 * @return {number}
 */

const value = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

const calc = (arr) => {
  let result = 0;
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] >= arr[i + 1]) {
      result += arr[i];
    } else {
      result -= arr[i];
    }
  }
  result += arr[arr.length - 1];

  return result;
};

var romanToInt = function (s) {
  let numberArr = [];
  for (let i = 0; i < s.length; i++) {
    numberArr = numberArr.concat(value[s[i]]);
  }
  return calc(numberArr);
};
