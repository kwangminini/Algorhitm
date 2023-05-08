function solution(N) {
  // Implement your solution here
  const binary = N.toString(2);
  let result = 0;
  const idxArr = [];
  let idx = 0;

  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === "1") {
      result = Math.max(result, i - idx);
      idx = i;
    }
  }

  return result > 0 ? result - 1 : result;
}
