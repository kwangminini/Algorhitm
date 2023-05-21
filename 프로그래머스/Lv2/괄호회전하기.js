function solution(s) {
  var answer = 0;
  let str = s;
  for (let i = 0; i < str.length; i++) {
    str = str.slice(1) + str.slice(0, 1);
    if (checkCorrect(str)) {
      answer += 1;
    }
  }
  return answer;
}

function checkCorrect(str) {
  const stack = [];
  let result = true;
  for (let i = 0; i < str.length; i++) {
    let pushFlag = true;
    if (i === 0 && ["]", ")", "}"].includes(str[i])) {
      result = false;
      break;
    }
    if (stack.at(-1) === "[" && str[i] === "]") {
      stack.pop();
      pushFlag = false;
    }
    if (stack.at(-1) === "(" && str[i] === ")") {
      stack.pop();
      pushFlag = false;
    }
    if (stack.at(-1) === "{" && str[i] === "}") {
      stack.pop();
      pushFlag = false;
    }
    if (pushFlag) {
      stack.push(str[i]);
    }
  }
  if (stack.length > 0) {
    result = false;
  }
  return result;
}
