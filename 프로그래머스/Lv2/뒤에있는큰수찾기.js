function solution(numbers) {
  var answer = new Array(numbers.length).fill(-1);
  const stack = [[numbers[0], 0]];
  for (let i = 1; i < numbers.length; i++) {
    for (let j = stack.length - 1; j >= 0; j--) {
      if (stack[j][0] < numbers[i]) {
        answer[stack[j][1]] = numbers[i];
        stack.pop();
      } else {
        break;
      }
    }

    stack.push([numbers[i], i]);
  }
  return answer;
}
