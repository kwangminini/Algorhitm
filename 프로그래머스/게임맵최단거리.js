function solution(maps) {
  const maxY = maps[0].length - 1;
  const maxX = maps.length - 1;
  const queue = [[0, 0, 1]];
  while (queue.length) {
    const [x, y, count] = queue.shift();
    if (x < 0 || x > maxX) {
      continue;
    }
    if (y < 0 || y > maxY) {
      continue;
    }
    if (maps[x][y] === 0) continue;
    if (x === maxX && y === maxY) {
      return count;
    }
    maps[x][y] = 0;
    queue.push([x + 1, y, count + 1]);
    queue.push([x - 1, y, count + 1]);
    queue.push([x, y + 1, count + 1]);
    queue.push([x, y - 1, count + 1]);
  }
  return -1;
}
