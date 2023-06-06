function solution(files) {
  const _files = files.map((file) => file.match(/(\D+)(\d+)/));
  return _files
    .sort((a, b) => {
      if (a[1].toLowerCase() > b[1].toLowerCase()) {
        return 1;
      } else if (a[1].toLowerCase() < b[1].toLowerCase()) {
        return -1;
      } else {
        return a[2] - b[2];
      }
    })
    .map((_file) => _file.input);
}
