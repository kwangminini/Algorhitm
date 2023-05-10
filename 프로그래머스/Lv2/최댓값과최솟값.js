function solution(s) {
  const numArr = s.split(" ").map(Number);
  numArr.sort((a, b) => a - b);
  return `${numArr[0]} ${numArr[numArr.length - 1]}`;
}
