function solution(k, score) {
  let answer = [];
  let queue = [];
  score.map((_score) => {
    if (queue.length < k) {
      queue = queue.concat(_score).sort((a, b) => a - b);
      answer = answer.concat(queue[0]);
    } else {
      if (queue[0] <= _score) {
        queue = queue.concat(_score).sort((a, b) => a - b);
        queue.shift();
        answer = answer.concat(queue[0]);
      } else {
        answer = answer.concat(queue[0]);
      }
    }
  });

  return answer;
}
