function solution(s) {
  const { str, count, zeroNum } = transform(s, 0, 0);
  return [count, zeroNum];
}
function transform(str, count, zeroNum) {
  if (str === "1") return { str, count, zeroNum };
  let zeroCount = 0;
  let strArr = str.split("");
  strArr = strArr.filter((str) => {
    if (str === "0") {
      zeroCount += 1;
    } else {
      return str;
    }
  });

  return transform(strArr.length.toString(2), count + 1, zeroNum + zeroCount);
}
