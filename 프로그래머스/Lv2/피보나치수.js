const divNum = 1234567;
function solution(n) {
  return fibo(n) % divNum;
}

function fibo(n) {
  const arr = [0, 1, 1];
  for (let i = 3; i <= n; i++) {
    arr.push((arr[i - 1] % divNum) + (arr[i - 2] % divNum));
  }
  return arr.at(-1);
}
