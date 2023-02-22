/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isMonotonic = function (nums) {
  let positive = 0;
  let negative = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] - nums[i + 1] >= 0) {
      positive += 1;
    }
    if (nums[i] - nums[i + 1] <= 0) {
      negative += 1;
    }
  }
  return positive === nums.length - 1 || negative === nums.length - 1;
};
