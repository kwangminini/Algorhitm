const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
let t = Number(input[0]);
let line = 1;

while (t--) {
  const [m, n, k] = input[line].split(" ").map(Number);
  const graph = [];
  let result = 0;
  for (let i = 0; i < n; i++) {
    graph[i] = new Array(m);
  }
  for (let i = 1; i <= k; i++) {
    let [y, x] = input[line + i].split(" ").map(Number);
    graph[x][y] = 1;
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (dfs(graph, n, m, i, j)) {
        result += 1;
      }
    }
  }
  line += k + 1;
  console.log(result);
}

function dfs(graph, n, m, x, y) {
  if (x < 0 || y < 0 || x >= n || y >= m) {
    return false;
  }
  if (graph[x][y] === 1) {
    graph[x][y] = -1;
    dfs(graph, n, m, x - 1, y);
    dfs(graph, n, m, x, y - 1);
    dfs(graph, n, m, x + 1, y);
    dfs(graph, n, m, x, y + 1);
    return true;
  }
  return false;
}
