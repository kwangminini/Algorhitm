function solution(k, score) {
  let answer = [];
  let queue = [];
  score.map((_score) => {
    if (queue.length <= k) {
      queue = queue.concat(_score);
      queue.sort();
      answer = answer.concat(queue[0]);
    } else {
      console.log("queue ## ", queue);
      // console.log("_score :: ", _score);
      if (queue[0] < _score) {
        queue = queue.concat(_score);
        // console.log("queue ## ", queue);
        queue.sort();
        answer = answer.concat(queue.shift());
      } else {
        answer = answer.concat(queue[0]);
      }
    }
  });

  return answer;
}
