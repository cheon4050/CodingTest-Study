// const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
// const n = +input[0];
// const screen = input.slice(1).map(v => v.split("").map(vv => +vv));

const screen=['11110000',
    '11110000',
    '00011100',
    '00011100',
    '11110000',
    '11110000',
    '11110011',
    '11110011'];

function genQuadTree(n){
    const quadTree = [];
    const recursion = (n, x, y) => {
        let total = 0;
        for(let i=0; i<n; i++) {
            for(let j=0; j<n; j++) {
                total += screen[y+j][x+i];
            }
        }
        if (total === 0) quadTree.push("0");
        else if (total === n*n) quadTree.push("1");
        else {
            n /= 2;
            quadTree.push("(");
            recursion(n, x, y);
            recursion(n, x+n, y);
            recursion(n, x, y+n);
            recursion(n, x+n, y+n);
            quadTree.push(")");
        }
    }
    recursion(n, 0, 0);
    console.log(quadTree.join(""));
};

genQuadTree(n);