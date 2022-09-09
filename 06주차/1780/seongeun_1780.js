//첫 번째 줄에 자연수 n을 입력받고, 그 다음줄에 공백으로 구분된 n개의 값들을 입력받을 때
let fs = require("fs");
let input = fs.readFileSync('./dev/stdin')
    .toString()
    .trim()
    .split("\n");
let paper = input
    .slice(1, input.length)
    .map((el) => el.split(" ").map((el) => Number(el)));
// let N=9;
// let arr=[N][N];
// paper=[[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,-1,-1,-1],
//     [0,0,0,1,1,1,-1,-1,-1],[1,1,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0],
//     [1,1,1,0,0,0,0,0,0],[0,1,-1,0,1,-1,0,1,-1],[0,-1,1,0,-1,1,0,-1,1],[0,1,-1,1,0,-1,0,1,-1]];

const countPaper = n => {
    const count = [0, 0, 0];
    const recursion = (n, x, y) => {
        const num = paper[y][x];
        let numCount = 0;
        for (let i=0; i<n; i++) {
            for (let j=0; j<n; j++) {
                if (paper[y+j][x+i] === num) numCount++;
                else break;
            }
        }
        if (numCount === n*n) count[num+1]++;
        else {
            n /= 3;
            for (let i=0; i<3; i++) {
                for (let j=0; j<3; j++) {
                    recursion(n, x+i*n, y+j*n);
                }
            }
        }
    }
    recursion(n, 0, 0);
    console.log(count.join("\n"));
};

countPaper(input);