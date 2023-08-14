function solution(name, yearning, photo) {
  var answer = [];
  for (const nameList of photo) {
    let count = 0;
    for (const nameItem of nameList) {
      const idx = name.findIndex((_name) => _name === nameItem);
      if (idx > -1) {
        count += yearning[idx];
      }
    }
    answer.push(count);
  }
  return answer;
}
