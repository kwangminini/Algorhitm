function solution(topping) {
  var answer = 0;
  const lStack = new Set();
  const rStack = new Set();
  const lArray = [];
  const rArray = [];
  const toppingReverse = [...topping].reverse();

  for (let i = 0; i < topping.length - 1; i++) {
    lStack.add(topping[i]);
    rStack.add(toppingReverse[i]);
    lArray.push(lStack.size);
    rArray.push(rStack.size);
  }
  rArray.reverse();
  for (let i = 0; i < lArray.length; i++) {
    if (lArray[i] === rArray[i]) {
      answer += 1;
    }
  }

  return answer;
}
