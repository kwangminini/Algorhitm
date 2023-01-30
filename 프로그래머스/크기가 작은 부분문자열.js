function solution(t, p) {
  let answer = 0;
  const partialStr = partial();
  answer = partialStr.filter((str) => str <= p).length;
  return answer;

  //부분문자열 추출
  function partial() {
    const tArr = [...t];
    const result = tArr.map((_t, idx) => {
      if (idx <= t.length - p.length) {
        return p.length > 1
          ? _t.concat(t.substring(idx + 1, idx + p.length))
          : _t;
      }
    });

    return result;
  }
}
