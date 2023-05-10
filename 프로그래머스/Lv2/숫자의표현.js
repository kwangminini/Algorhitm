function solution(n) {
  let result = 1;
  let start = 1;
  while (start < n) {
    let count = 0;
    for (let i = start; i <= n; i++) {
      count += i;
      if (count === n) {
        result += 1;
      }
      if (count > n) {
        break;
      }
    }
    start += 1;
  }
  return result;
}
