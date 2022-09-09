// const filePath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';
// const input = require('fs').readFileSync(filePath).toString();
//
// const N = Number(input);
const n=6;
// const n = Number(require('fs').readFileSync('dev/stdin'));
const solution = (n) => {
    const binArr = n.toString(2).split("");
    //n보다 작은 2^x 값 빼기
    binArr.shift();
    const answer = parseInt(binArr.join(""), 2);

    return answer ? answer * 2 : n;
}
console.log(solution(n));

/**
 * n       answer     role
 * 1            1       1
 * 1,2          2           2
 * 1,2,3        2         (3-2)*2
 * 1,2,3,4      4        4
 * 1,2,3,4,5    2        (5-4)*2
 * 1,2,3,4,5,6  4        (6-4)*2
 *                      (7-4)*2
 *                      8
 *                      (9-8)*2
 *
 * n이  2제곱일 경우 값이 n
 * (n-(n보다 작은 2의 제곱)) *2
 * **/

