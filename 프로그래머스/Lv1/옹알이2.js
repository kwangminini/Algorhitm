function solution(babbling) {
  var answer = 0;
  const test = ["aya", "ye", "woo", "ma"];
  babbling.forEach((str, idx) => {
    test.forEach((_test) => {
      let idx = str.indexOf(_test);
      if (idx > -1) {
        str = str.slice(idx + _test.length, str.length);
      }
    });
    if (str === "") {
      answer += 1;
    }
  });
  return answer;
}
