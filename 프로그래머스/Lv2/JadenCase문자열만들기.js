function solution(s) {
  const lowerS = s.toLowerCase();
  const strArr = lowerS.split(" ").map((str) => {
    if (str) {
      return str[0].toUpperCase() + str.substr(1, str.length - 1);
    }
    return str;
  });
  return strArr.join(" ");
}
