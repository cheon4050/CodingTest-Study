const N=5;
let A=[4,1,5,2,3];
const M=5;
let B=[1,3,7,9,5];

// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// const [N, A, M, B] = input.map(v => v.split(" "));

const array = new Set(A);
const result = B.map(v => array.has(v) ? 1 : 0);
console.log(result.join("\n"));

// for문과 if 문을 이용해서 짰는데 시간 초과가 떴다.
//set메서드를 쓰면 has로 포함되어있는 수가 있는지 검사가능!