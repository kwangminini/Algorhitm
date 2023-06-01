function solution(A) {
  // Implement your solution here
  A.sort((a, b) => a - b);
  const result = [A[0]];
  for (var i = 1; i < A.length; i++) {
    if (result[result.length - 1] === A[i]) {
      result.pop();
    } else {
      result.push(A[i]);
    }
  }
  return result[0];
}
