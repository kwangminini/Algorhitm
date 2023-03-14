function solution(n, times) {
  let answer = 0;
  const timesLen = times.length;
  const maxAnswer = times.reduce((acc, cur) => Math.max((acc, cur)));
  let low = 0;
  let high = maxAnswer * n;
  answer = high;
  while (low <= high) {
    let mid = parseInt((low + high) / 2);
    let acceptCount = 0;
    for (let i = 0; i < timesLen; i++) {
      acceptCount += parseInt(mid / times[i]);
    }
    if (acceptCount < n) {
      low = mid + 1;
    } else {
      high = mid - 1;
      if (answer > mid) {
        answer = mid;
      }
    }
  }
  return answer;
}
