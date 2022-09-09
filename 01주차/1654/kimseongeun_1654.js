const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [K, N] = input.shift().split(' ');
const lines = input.map(Number).sort((a,b) => a-b);


function solution(k, n, nums) {
    let answer = 0;
    let start = 0;
    let end = 10e9; //시작점을 0, 끝 점을 10e9

    function count(mid) {
        let result = 0;
        for (const x of nums) { //x : xcm씩 자른다고 가정했을때 나오는거
            result += Math.floor(x / mid);
        }
        return result;
    }

    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        if (count(mid) < n) {
            end = mid - 1;
        } else {
            answer = mid;
            start = mid + 1;
        }
    }

    return answer;
}
/*
4,11에 [802,743,457,539]
* mid로 나눠진 값으로 (몫)을 더한게 11일경우
* 11일 경우 중 mid가 제일 큰 경우

-> 그니까 랜선은 xcm 만큼 잘랐을 때 각 랜선에서 얻은 랜선의 개수가 n개보다 많아야 한다.
n개보다 작다면 너무 길게 자른 것이기 때문에 길이를 줄여야 한다.
n개보다 크거나 같으면 개수는 충분하기 때문에 길이를 더 늘려서 답을 찾을 수 있는지 확인한다.
xcm씩 잘랐을 때 나오는 랜선의 개수를 구하기 위해 각 랜선을 x로 나누었을 때 몫을 취한다.
* */