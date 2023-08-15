function solution(N, stages) {
  var answer = new Array(N + 1).fill(1).map((_, idx) => [idx + 1, 0]);
  let people = stages.length;
  stages
    .sort((a, b) => a - b)
    .forEach((s) => {
      answer[s - 1][1] += 1;
    });
  const result = [];
  for (let i = 0; i < answer.length - 1; i++) {
    const _arr = [...answer[i]];
    answer[i][1] = answer[i][1] / people;
    result.push(answer[i]);
    people -= _arr[1];
  }

  return result
    .sort((a, b) => {
      if (a[1] === b[1]) {
        return a[0] - b[0];
      }
      return b[1] - a[1];
    })
    .map((x) => x[0]);
}
