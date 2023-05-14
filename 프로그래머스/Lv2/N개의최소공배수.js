const answer = [];
function solution(arr) {
  arr.sort((a, b) => a - b);
  answer.push(arr[0]);
  for (let i = 1; i < arr.length; i++) {
    leastCommonMultiple(answer.pop(), arr[i]);
  }
  return answer[0];
}
function leastCommonMultiple(num, num2) {
  const maxNum = Math.max(num, num2);
  const minNum = Math.min(num, num2);
  let flag = true;
  let count = 1;
  if (maxNum % minNum === 0) {
    answer.push(maxNum);
  } else {
    while (flag) {
      const compNum = minNum * count;
      if (compNum % maxNum === 0) {
        answer.push(compNum);
        flag = false;
      } else {
        count += 1;
      }
    }
  }
}
