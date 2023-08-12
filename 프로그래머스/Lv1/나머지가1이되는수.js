function solution(n) {
  for (let i = 1; i < n; i++) {
    if (parseInt(n % i) === 1) {
      return i;
    }
  }
}
