function solution(elements) {
  const arr = new Set();
  const doubleElements = [...elements, ...elements];

  let count = 1;
  while (count <= elements.length) {
    for (let i = 0; i < elements.length; i++) {
      let num = 0;
      for (let j = i; j < i + count; j++) {
        num += doubleElements[j];
      }
      arr.add(num);
    }
    count += 1;
  }

  return arr.size;
}
