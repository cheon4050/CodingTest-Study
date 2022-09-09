// let fs = require('fs');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const bfs = (graph, startNode) => {
    const visited = [];
    let needVisit = [];
    needVisit.push(startNode);
    while(needVisit.length !==0){
        const node = needVisit.shift();
        if(!visited.includes(node)){
            //    v 방문한 사실을 저장;
            //결과 변수 값에 +1해서 저장;
            visited.push(node);
            needVisit = [...needVisit, ...graph[node]];
        }
    }
    return visited;
};
let count = Number(input.shift());
let edge = Number(input.shift());
let grph = [...Array(count + 1)].map(e => []);
for(let i = 0 ; i < edge; i++){
    let [from, to] = input[i].split(' ').map(Number);
    grph[from].push(to); grph[to].push(from);
}

console.log(bfs(grph, 1).length - 1);
