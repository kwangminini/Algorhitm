function solution(s) {
  const wordList = s.split(" ");
  let answer = "";
  for (let j = 0; j < wordList.length; j++) {
    if (wordList[j]) {
      for (let i = 0; i < wordList[j].length; i++) {
        if (i % 2 === 0) {
          answer += wordList[j][i].toUpperCase();
        } else {
          answer += wordList[j][i].toLowerCase();
        }
      }
    }
    if (j !== wordList.length - 1) {
      answer += " ";
    }
  }
  return answer;
}
