// const fs = require("fs");
// const filePath =
//     process.platform === "linux" ? "/dev/stdin" : __dirname + "/input.txt";
// let input = fs.readFileSync(filePath).toString().split("\n");
//
// let count = input[0];
// let numbers = [];
//
// for (let i = 1; i < input.length; i++) {
//     if (input[i] !== "") {
//         numbers.push(input[i].split(" ").map((str) => Number(str)));
//     }
// }

function solution(n, numbers) {
    let answer = 1;
    numbers.sort((a, b) => {
        if (a[1] === b[1]) return a[0] - b[0];
        else return a[1] - b[1];
    });

    let currentEndTime = numbers[0][1];

    for (let i = 1; i < n; i++) {
        const [start, end] = numbers[i];
        if (start >= currentEndTime) {
            currentEndTime = end;
            answer += 1;
        }
    }

    console.log(answer);
}

solution(count, numbers);