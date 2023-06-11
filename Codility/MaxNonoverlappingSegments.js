// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, B) {
  // Implement your solution here
  if (A.length < 1) {
    return 0;
  }
  if (A.length < 2) {
    return 1;
  }
  let end = 0;
  let count = 1;
  for (let i = 1; i < A.length; i++) {
    if (B[end] < A[i]) {
      count += 1;
      end = i;
    }
  }
  return count;
}
