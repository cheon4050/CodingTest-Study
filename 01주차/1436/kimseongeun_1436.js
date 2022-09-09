// const fs = require('fs');
// let input = parseInt(fs.readFileSync('/dev/stdin').toString().trim());
let input=3;
let num = 666;
let count = 1;
while (count !== input) {
    num++; if (String(num).includes("666")) count++;
}
console.log(num);

//num을 1씩 늘려가면서 num내에 연속된 666이 존재할 때마다
// 카운트를 증가시켜 목표한 카운트(n)에 도달할 때까지 반복