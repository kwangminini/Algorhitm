function solution(d, budget) {
  d.sort((a, b) => a - b);
  let acc = 0;

  for (let i = 0; i < d.length; i++) {
    if (acc + d[i] > budget) {
      return i;
    }
    acc += d[i];
  }

  return d.length;
}
