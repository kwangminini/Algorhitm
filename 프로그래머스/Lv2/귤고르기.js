function solution(k, tangerine) {
  var answer = 0;
  const numberObj = {};
  for (const num of tangerine) {
    if (numberObj[num]) {
      numberObj[num] += 1;
    } else {
      numberObj[num] = 1;
    }
  }
  const numberValueArr = Object.values(numberObj).sort((a, b) => b - a);
  let checkNum = 0;
  for (let i = 0; i < numberValueArr.length; i++) {
    checkNum += numberValueArr[i];
    if (checkNum >= k) {
      answer = i + 1;
      break;
    }
  }

  return answer;
}
