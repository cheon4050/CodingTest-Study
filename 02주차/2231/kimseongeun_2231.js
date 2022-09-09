// const fs = require('fs');
// const input = parseInt(fs.readFileSync('/dev/stdin').toString().trim());
const input = 216;
const arr = [];

function sum(n) {
    const N = n.toString().split('');

    return n + N.reduce((acc, num) => (acc += parseInt(num)), 0);
}

for (let i = 1; i <= input; i++) {
    if (sum(i) === input) {
        arr.push(i);
    }
}

if (arr.length) {
    console.log(Math.min.apply(null, arr));
} else {
    console.log(0);
}
