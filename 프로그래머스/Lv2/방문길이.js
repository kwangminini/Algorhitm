function solution(dirs) {
  var answer = 0;
  const visited = new Set();
  let x = 5;
  let y = 5;
  for (let i = 0; i < dirs.length; i++) {
    [_x, _y] = direct(x, y, dirs[i]);
    if (_x < 0 || _x > 10 || _y < 0 || _y > 10) {
      continue;
    } else {
      if (!visited.has(x + "" + y + _x + _y)) {
        visited.add(x + "" + y + _x + _y);
        visited.add(_x + "" + _y + x + y);
      }
      x = _x;
      y = _y;
    }
  }
  return visited.size / 2;
}

function direct(x, y, type) {
  const _direct = {
    L: [x - 1, y],
    U: [x, y + 1],
    R: [x + 1, y],
    D: [x, y - 1],
  };
  return _direct[type];
}
