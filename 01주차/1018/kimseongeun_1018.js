//브루트포스-완전탐색
const fs=require('fs');
const readFileSyncAddress='/dev/stdin';
//const readFileSyncAddress='input.txt';

let input=fs.readFileSync(readFileSyncAddress).toString().trim().split('\n');

function solution(input){
    [size, ...arr]=input;
    [row, col]=size.split(' ');
    arr=arr.map(str => str.trim('\r').split(''));
    const answer=[];
    const line=['WBWBWBWB','BWBWBWBW'];

    for(let i=0; i<=row-8; i++){
        for(let j=0; j<= col-8; j++){
            for(let z=0; z<2; z++){
                let count=0;
                for(let x=0; x<8; x++){
                    for(let y=0; y<8; y++){
                        const current=arr[i+x][j+y];
                        if(current !== line[(x+z)%2][y]) count++;
                    }
                }
                answer.push(count);
            }
        }
    }
    return Math.min(...answer);
}

console.log(solution(input));