/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
  let left = 0;
  let right = 1;

  while (right < nums.length) {
    if (nums[left] === 0 && nums[right] !== 0) {
      const temp = nums[right];
      nums[right] = nums[left];
      nums[left] = temp;
      left += 1;
    }
    if (nums[left] !== 0) {
      left += 1;
    }
    right += 1;
  }
  return nums;
};
