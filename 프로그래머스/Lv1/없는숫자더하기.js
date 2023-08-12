function solution(numbers) {
  let arr = Array.from({ length: 9 }, (_, index) => index + 1);

  for (const num of numbers) {
    const numIdx = arr.indexOf(num);
    if (numIdx > -1) {
      arr = arr.filter((_, idx) => idx !== numIdx);
    }
  }
  return arr.reduce((acc, cur) => acc + cur, 0);
}
