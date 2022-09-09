let fs = require("fs");
let input = fs.readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");
let arr = input
    .slice(1, input.length)
    .map((el) => el.split(" ").map((el) => Number(el)));
// let arr = [[1,0],[5],[4,2],[1,2,3,4],[6,0],[1,1,9,1,1,1]];
let temp = [];

for (let i = 0; i < arr.length; i += 2) {
    arr[i + 1][arr[i][1]] = String(arr[i + 1][arr[i][1]]);
    temp.push(arr[i + 1]);
}

for (let i = 0; i < temp.length; i++) {
    let count = 1;
    let box = temp[i];
    let test = temp[i].map((el) => Number(el));
    while (true) {
        let maxIndex = test.indexOf(Math.max(...test)); //최댓값의 index값 뽑기
        if (maxIndex !== 0) {
            test = test.slice(maxIndex, test.length).concat(test.slice(0, maxIndex));
            //test에는 최댓값이 0번째 인덱스로 오도록 넣어줌
            box = box.slice(maxIndex, box.length).concat(box.slice(0, maxIndex));
            //box도 동일
        }
        if (typeof box[0] === "string") {
            console.log(count);
            break;
        } else {
            test.shift(); //맨 첫번째부터 제외 시키기 시작
            box.shift(); //맨 첫번째부터 제외 시키기 시작
            count++;
        }
    }
}