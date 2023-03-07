/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  const resultObj = {};
  nums.map((num) => {
    resultObj[num] = resultObj[num] ? resultObj[num] + 1 : 1;
  });

  return Object.keys(resultObj).find((key) => resultObj[key] === 1);
};
