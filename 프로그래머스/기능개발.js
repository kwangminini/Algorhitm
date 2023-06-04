function solution(progresses, speeds) {
  var answer = [];
  const distribution = [];
  var successTime = 100;
  for (let i = 0; i < progresses.length; i++) {
    const remain = successTime - progresses[i];
    distribution.push(getDistribution(remain, speeds[i]));
  }

  let maxTime = distribution[0];
  let count = 1;
  for (let i = 1; i < distribution.length; i++) {
    if (distribution[i] > maxTime) {
      answer.push(count);
      count = 1;
      maxTime = distribution[i];
    } else {
      count++;
    }
  }
  answer.push(count);
  return answer;
}

function getDistribution(remain, speed) {
  return parseInt(remain / speed) + (remain % speed ? 1 : 0);
}
