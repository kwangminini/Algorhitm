/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function (nums) {
  let result = 0;
  nums.sort((a, b) => (a > b ? 1 : -1));
  for (let i = 0; i < nums.length; i = i + 2) {
    result += Math.min(nums[i], nums[i + 1]);
  }
  return result;
};
