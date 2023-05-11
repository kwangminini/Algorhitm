function solution(people, limit) {
  var answer = 0;
  people.sort((a, b) => a - b);
  while (people.length > 0) {
    if (people[0] + people.at(-1) <= limit) {
      people.shift();
      people.pop();
    } else {
      people.pop();
    }
    answer += 1;
  }

  return answer;
}
