function solution(food) {
  const result = [];
  for (let i = 1; i < food.length; i++) {
    const divNum = parseInt(food[i] / 2);
    for (let j = 0; j < divNum; j++) {
      result.push(i);
    }
  }
  const left = result.join("");
  const right = result.reverse().join("");
  return left + "0" + right;
}
