function solution(a, b, n) {
  let answer = calc(n, 0);

  return answer;

  function calc(number, count) {
    const receivedItem = parseInt(number / a) * b;
    const remainder = number % a;
    if (number >= a) {
      count += receivedItem;
      return calc(receivedItem + remainder, count);
    } else {
      return count;
    }
  }
}
