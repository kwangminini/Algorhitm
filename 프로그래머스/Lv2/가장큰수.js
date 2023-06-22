function solution(numbers) {
  let answer = "";

  const strNumbers = numbers.map(String);

  strNumbers.sort((a, b) => b + a - (a + b));
  answer = strNumbers.join("");
  if (Number(answer) === 0) return "0";
  return answer;
}
