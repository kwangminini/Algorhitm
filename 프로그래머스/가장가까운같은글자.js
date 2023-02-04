function solution(s) {
  let answer = [-1];
  for (let i = 1; i < s.length; i++) {
    answer = answer.concat(findLetter(i));
  }
  return answer;

  function findLetter(idx) {
    const str = s.substring(0, idx);
    const reverseStr = str.split("").reverse().join("");
    return reverseStr.indexOf(s[idx]) > -1
      ? reverseStr.indexOf(s[idx]) + 1
      : reverseStr.indexOf(s[idx]);
  }
}
