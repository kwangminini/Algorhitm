function solution(fees, records) {
  let answer = [];
  const [defaultTime, defaultFee, unitTime, unitFee] = fees;
  const carNumArr = new Array(9999).fill(-1);
  const inArr = new Array(9999).fill(-1);
  for (const record of records) {
    let [time, carNum, history] = record.split(" ");
    carNum = Number(carNum);
    if (history === "IN") {
      inArr[carNum] = timeCalc(time);
    }
    if (history === "OUT") {
      if (carNumArr[carNum] > -1) {
        carNumArr[carNum] += timeCalc(time) - inArr[carNum];
      } else {
        carNumArr[carNum] = timeCalc(time) - inArr[carNum];
      }
      inArr[carNum] = -1;
    }
  }
  inArr.map((inItem, idx) => {
    if (inItem > -1) {
      if (carNumArr[idx] > -1) {
        carNumArr[idx] += timeCalc("23:59") - inItem;
      } else {
        carNumArr[idx] = timeCalc("23:59") - inItem;
      }
    }
  });
  answer = carNumArr
    .filter((x) => x > -1)
    .map((accTime) => {
      if (accTime < defaultTime) return defaultFee;
      return (
        defaultFee + Math.ceil((accTime - defaultTime) / unitTime) * unitFee
      );
    });

  return answer;
}

function timeCalc(time) {
  const [hour, minute] = time.split(":");
  return Number(minute) + Number(hour) * 60;
}
