/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  if (numRows === 1) return [[1]];
  if (numRows === 2) return [[1], [1, 1]];
  const arr = [[1], [1, 1]];

  while (arr.length < numRows) {
    const last = arr.at(-1);
    const base = [1];
    for (let i = 0; i < last.length - 1; i++) {
      base.push(last[i] + last[i + 1]);
    }
    base.push(1);
    arr.push(base);
  }
  return arr;
};
