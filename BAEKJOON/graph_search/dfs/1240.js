const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const [n, m] = input[0].split(" ").map(Number);
const graph = [];
const distance = [];
let visited = new Array(n + 1).fill(false);
for (let i = 1; i <= n; i++) {
  distance[i] = new Array(n);
  graph[i] = [];
}
for (let i = 1; i < n; i++) {
  const [x, y, d] = input[i].split(" ").map(Number);
  graph[x].push(y);
  graph[y].push(x);
  distance[x][y] = d;
  distance[y][x] = d;
}
for (let i = 0; i < m; i++) {
  const [x, y] = input[n + i].split(" ").map(Number);
  dfs(x, y, 0);
  visited = new Array(n + 1).fill(false);
}
function dfs(x, y, d) {
  for (const _y of graph[x]) {
    if (!visited[_y]) {
      visited[x] = true;
      if (_y === y) {
        return console.log(d + distance[x][_y]);
      }
      dfs(_y, y, d + distance[x][_y]);
    }
  }
  return;
}
