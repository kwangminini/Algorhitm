function solution(s) {
  if (s.length % 2 > 0 || s[0] === ")") return false;
  let answer = true;
  const stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push("(");
    } else if (stack.length > 0) {
      stack.pop();
    } else {
      return false;
    }
  }
  answer = stack.length === 0;

  return answer;
}
