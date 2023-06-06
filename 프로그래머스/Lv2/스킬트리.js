function solution(skill, skill_trees) {
  var answer = 0;

  for (let i = 0; i < skill_trees.length; i++) {
    let skillArr = [];
    for (let j = 0; j < skill_trees[i].length; j++) {
      if (skill.indexOf(skill_trees[i][j]) > -1) {
        skillArr.push(skill.indexOf(skill_trees[i][j]));
      }
    }
    if (isOrderAsc(skillArr)) {
      answer++;
    }
  }
  return answer;
}

function isOrderAsc(arr) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== i) return false;
  }
  return true;
}
