function solution(numbers, target) {
  let queue = [numbers[0], -1 * numbers[0]];

  for (let i = 1; i < numbers.length; i++) {
    let newQueue = [];
    for (let j = 0; j < queue.length; j++) {
      newQueue.push(queue[j] + numbers[i]);
      newQueue.push(queue[j] - numbers[i]);
    }
    queue = newQueue;
  }

  return queue.filter((q) => q === target).length;
}
