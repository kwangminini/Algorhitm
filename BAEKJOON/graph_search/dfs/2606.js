const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const cumputerNum = Number(input[0]);
const m = Number(input[1]);
let graph = [];
let result = 0;
const visited = new Array(cumputerNum + 1).fill(false);
for (let i = 1; i <= cumputerNum; i++) graph[i] = [];
for (let i = 2; i <= m + 1; i++) {
  const [x, y] = input[i].split(" ").map(Number);
  graph[x].push(y);
  graph[y].push(x);
}
dfs(1);

function dfs(x) {
  visited[x] = true;
  result += 1;
  for (y of graph[x]) {
    if (!visited[y]) {
      dfs(y);
    }
  }
}
console.log(result - 1);
