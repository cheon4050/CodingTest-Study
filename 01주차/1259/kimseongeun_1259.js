let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
input.pop(); //0이 포함되지 않는다고 나와있기에 마지막꺼 빼기

for (let i = 0; i < input.length; i++) {
    let reverseStr = input[i].split("").reverse().join("");
    console.log(input[i] === reverseStr ? "yes" : "no");
}