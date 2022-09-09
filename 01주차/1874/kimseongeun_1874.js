var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');
var cases = input[0];
var arr = [];
var stack = [];
var answer = '';
for(var i=0; i<cases; i++){
    arr[i] = i+1;
}
for(var j=1; j<=cases; j++){ //4
    var count = 1;
    while(count <= cases && stack[stack.length-1] != input[j]){
        stack.push(arr.shift());
        answer += '+\n';
        count++;
    }
    if(stack[stack.length-1] == input[j]){
        stack.pop();
        answer += '-\n';
    }else{
        answer = 'NO';
        break;
    }
}
console.log(answer);


/*
* 입력받는 배열의 길이를 cases로 받아서, 해당 길이만큼 1부터 cases까지의 배열을 arr로 선언해준다
배열의 길이만큼 돌면서 stack의 마지막 값이 input[j]값과 같지않다면 arr에 있는 요소를 계속 stack에 push해준다.
push 할 때에는 +값이 들어가야하므로, answer에 +값을 추가해줌
만약 stack의 마지막 값이 input[j]값과 같아서 while문에서 빠져나오게 된다면,
* stack에서 해당 값인 stack의 마지막 값을 pop함수로 꺼내주고, answer에는 -를 추가해주고
하지만, stack의 마지막 값이 input[j]와 같지 않다면, answer에는 NO를 입력해서 반환해줌.
*
* */