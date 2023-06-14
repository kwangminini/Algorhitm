function solution(s) {
  var answer = [];
  let open = false;
  let part = [];
  var result = [];
  let test = "";
  for (let i = 1; i < s.length - 1; i++) {
    if (open) {
      if (s[i] !== "," && s[i] !== "}") {
        test += s[i];
      }
      if (s[i] === ",") {
        part.push(Number(test));
        test = "";
      }
      if (s[i] === "}") {
        if (test !== "") {
          part.push(Number(test));
        }
        open = false;
        test = "";
        answer.push(part);
        part = [];
      }
    }
    if (s[i] === "{") {
      open = true;
    }
  }
  answer.sort((a, b) => a.length - b.length);
  for (const arr of answer) {
    for (const arr2 of arr) {
      if (!result.includes(arr2)) {
        result.push(arr2);
      }
    }
  }

  return result;
}
