function solution(n) {
  let answer = 0;
  let nextNum = n;
  while (answer === 0) {
    nextNum += 1;
    if (getOneCount(nextNum) === getOneCount(n)) {
      answer = nextNum;
    }
  }
  return answer;
}

function getOneCount(num) {
  const binary = num.toString(2);
  let result = 0;
  for (const value of binary) {
    if (value === "1") {
      result += 1;
    }
  }
  return result;
}
