function solution(dartResult) {
  var answer = [];
  const _dartResult = splitByCharacter(dartResult);
  for (let i = 0; i < _dartResult.length; i++) {
    let result = _dartResult[i];
    if (!isNaN(result)) {
      answer.push(Number(result));
    } else {
      for (let j = 0; j < result.length; j++) {
        if (result[j] === "D") {
          answer[answer.length - 1] = answer[answer.length - 1] ** 2;
        }
        if (result[j] === "T") {
          answer[answer.length - 1] = answer[answer.length - 1] ** 3;
        }
        if (result[j] === "#") {
          answer[answer.length - 1] = answer[answer.length - 1] * -1;
        }
        if (result[j] === "*") {
          answer[answer.length - 1] = answer[answer.length - 1] * 2;
          if (answer.length > 1) {
            answer[answer.length - 2] = answer[answer.length - 2] * 2;
          }
        }
      }
    }
  }
  return answer.reduce((acc, cur) => acc + Number(cur));
}
function splitByCharacter(inputString) {
  return inputString.split(/(\D+)/).filter(Boolean);
}
