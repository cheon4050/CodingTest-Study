const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const n = +input[0];
const paper = input.slice(1).map(v => v.split(" ").map(vv => +vv));
const countPaper = n => {
    const count = [0, 0];
    const recursion = (n, x, y) => {
        let total = 0;
        for(let i=0; i<n; i++) {
            for(let j=0; j<n; j++) {
                total += paper[y+j][x+i];
            }
        }
        if (total === 0) count[0]++;
        else if (total === n*n) count[1]++;
        else {
            n /= 2;
            recursion(n, x, y);
            recursion(n, x+n, y);
            recursion(n, x, y+n);
            recursion(n, x+n, y+n);
        }
    }
    recursion(n, 0, 0);
    console.log(count.join("\n"));
};
countPaper(n);

/**
 * recursion에서 현재 종이의 모든 숫자를 더한 값이 0이면 흰색 개수를 증가시키고,
 * n*n이면 파란색 개수를 증가시키고, 둘 다 아니라면 종이를 4분할 하여 각각의 종이별로
 * 다시 recursion을 재귀호출하였다.
 *
 * **/