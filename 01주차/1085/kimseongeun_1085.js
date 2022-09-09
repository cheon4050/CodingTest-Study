const fs=require('fs');
const readFileSyncAddress='/dev/stdin';

// For local test
const input = fs.readFileSync(readFileSyncAddress).toString().trim().split(' ');
const x = input[0];
const y = input[1];
const w = input[2];
const h = input[3];
const counters = [x, y, w - x, h - y]; //직사각형을 벗어날 수 있는 이동 값

console.log(Math.min.apply(null, counters));