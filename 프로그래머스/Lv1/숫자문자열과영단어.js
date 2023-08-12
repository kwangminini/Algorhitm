function solution(s) {
  let answer = "";
  const wordObj = {
    zero: 0,
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
  };
  const sArr = s.split("");
  let curNum = "";

  for (const n of s) {
    if (isNaN(n)) {
      curNum += n;
      const wordObjKeyArr = Object.keys(wordObj);
      if (wordObjKeyArr.indexOf(curNum) > -1) {
        answer += wordObj[wordObjKeyArr[wordObjKeyArr.indexOf(curNum)]];
        curNum = "";
      }
    }
    if (!isNaN(n)) {
      answer += n;
    }
  }
  return Number(answer);
}
