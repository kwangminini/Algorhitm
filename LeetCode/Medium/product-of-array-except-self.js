/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const leftArr = [];
  const rightArr = [];
  const result = [];

  nums.reduce((acc, cur, idx) => {
    if (idx === 0) {
      leftArr.push(1);
    } else {
      leftArr.push(acc);
    }
    return acc * cur;
  }, 1);

  nums.reverse().reduce((acc, cur, idx) => {
    if (idx === 0) {
      rightArr.push(1);
    } else {
      rightArr.push(acc);
    }
    return acc * cur;
  }, 1);

  nums.map((num, idx) => {
    result.push(leftArr[idx] * rightArr[nums.length - idx - 1]);
  });

  return result;
};
