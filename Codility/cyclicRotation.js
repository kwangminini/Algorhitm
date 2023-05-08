function solution(A, K) {
  // Implement your solution here
  const result = Array(A.length);
  for (let i = 0; i < A.length; i++) {
    result[calcIdx(i, K, A)] = A[i];
  }
  return result;
}
function calcIdx(idx, k, a) {
  let result = idx + k;
  if (idx + k >= a.length) {
    result = result % a.length;
  }
  return result;
}
