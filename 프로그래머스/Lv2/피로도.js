let count = 0;
function solution(k, dungeons) {
  const visited = new Array(dungeons.length).fill(false);
  dfs(k, dungeons, visited);
  return count;
}

function dfs(k, dungeons, visited) {
  const visitedNum = visited.filter((v) => v).length;
  if (count < visitedNum) {
    count = visitedNum;
  }

  for (let i = 0; i < dungeons.length; i++) {
    if (!visited[i] && k >= dungeons[i][0]) {
      visited[i] = true;
      dfs(k - dungeons[i][1], dungeons, visited);
      visited[i] = false;
    }
  }
}
