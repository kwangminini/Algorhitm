function solution(n, a, b) {
  var answer = 1;
  while (n > 1) {
    const max = Math.max(a, b);
    const min = Math.min(a, b);
    if (max - min === 1 && (min % 2) - (max % 2) === 1) {
      break;
    }
    answer += 1;
    n = parseInt(n / 2);
    a = initNum(a);
    b = initNum(b);
  }

  return answer;
}

function initNum(num) {
  if (num % 2 === 0) {
    return parseInt(num / 2);
  }
  return parseInt(num / 2) + 1;
}
