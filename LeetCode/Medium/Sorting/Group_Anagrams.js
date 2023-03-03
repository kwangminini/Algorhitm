/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const resultObj = {};
  for (const str of strs) {
    const arrToStr = str.split("").sort().join("");
    if (!Object.keys(resultObj).includes(arrToStr)) {
      resultObj[arrToStr] = [str];
    } else {
      resultObj[arrToStr].push(str);
    }
  }
  return Object.values(resultObj).sort();
};
