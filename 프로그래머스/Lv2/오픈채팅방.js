function solution(record) {
  var answer = [];
  const idObj = {};
  for (const recordText of record) {
    const [activate, id, name] = recordText.split(" ");
    answer.push([activate, id]);
    if (activate !== "Leave") {
      idObj[id] = name;
    }
  }
  let result = [];
  for (const _record of answer) {
    if (_record[0] === "Enter") {
      result.push(`${idObj[_record[1]]}님이 들어왔습니다.`);
    } else if (_record[0] === "Leave") {
      result.push(`${idObj[_record[1]]}님이 나갔습니다.`);
    }
  }

  return result;
}
