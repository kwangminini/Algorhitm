function solution(brown, yellow) {
  var answer = [];
  const arr = divisors(yellow);
  for (const [x, y] of arr) {
    if (x + 2 < brown) {
      if ((x + 2) * 2 + y * 2 === brown) {
        answer.push(x + 2, y + 2);
        break;
      }
    }
  }

  return answer;
}

function divisors(num) {
  if (num === 1) return [[1, 1]];
  const arr = [];
  for (let i = 1; i < num; i++) {
    if (num % i === 0) {
      const position = [i, parseInt(num / i)].sort((a, b) => b - a);
      arr.push(position);
    }
  }
  return arr;
}
