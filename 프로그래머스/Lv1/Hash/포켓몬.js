function solution(nums) {
  var answer = new Set();
  for (const num of nums) {
    answer.add(num);
  }
  const n = parseInt(nums.length / 2);

  return answer.size > n ? n : answer.size;
}
