/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const obj = {};
  for (let i = 0; i < nums.length; i++) {
    if (Object.values(obj).includes(nums[i])) {
      return [nums.indexOf(target - nums[i]), i];
    } else {
      obj[nums[i]] = target - nums[i];
    }
  }
};
