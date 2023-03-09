/**
 * @param {string[]} operations
 * @return {number}
 */
var calPoints = function (operations) {
  const result = [];
  for (let i = 0; i < operations.length; i++) {
    if (["C", "D", "+"].includes(operations[i])) {
      if (operations[i] === "C") {
        result.pop();
      } else if (operations[i] === "D") {
        result.push(result[result.length - 1] * 2);
      } else {
        result.push(result[result.length - 1] + result[result.length - 2]);
      }
    } else {
      result.push(Number(operations[i]));
    }
  }
  return result.length > 0 ? result.reduce((acc, cur) => acc + cur) : 0;
};
