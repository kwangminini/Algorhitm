function solution(cards1, cards2, goal) {
  var answer = "";
  for (const word of goal) {
    if (word === cards1[0]) {
      cards1.shift();
    } else if (word === cards2[0]) {
      cards2.shift();
    } else {
      return "No";
    }
  }
  return "Yes";
}
