function solution(s) {
  const stack = [];
  if (s.length % 2 > 0) return 0;
  for (const str of s) {
    if (stack[stack.length - 1] === str) stack.pop();
    else stack.push(str);
  }
  return stack.length === 0 ? 1 : 0;
}
