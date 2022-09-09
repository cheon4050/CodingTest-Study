const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const isPrime = (num) => {
    if(num === 1) //1의경우 소수가 아니므로 별도로 조건문을 걸어줬다.
        return false;
    for(var i=2; i<=Math.sqrt(num); i++){
        if((num%i)===0)
            return false;
        //2부터 num의 제곱근까지의 값으로 나눠서 나누어 떨어지는 것이 있으면 소수가 아닐 것이다.
        //소수는 1과 자기 자신으로만 나눠지니까
    } return true;
}

const [M,N] = input.shift().split(' ').map(e=>parseInt(e));

for(var i=M; i<=N; i++)
    isPrime(i) ? console.log(i) : null;


/**
 * 에라토스테네스의 체
 * 2부터 끝숫자의 제곱근까지 보며 값이 있으면 그 값을 제외하고 그값의 배수들을 모두 false 시킨다.
 *
 * let fs = require('fs');
 * let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
 * const [n,m] = input.shift().split(' ').map(e=>parseInt(e));
 * const arr = Array.from(Array(m+1).keys())
 * for(let i=2; i<=Math.sqrt(m); i++){
 *  if(arr[i])
 *      for(let j = i*i; j<=m; j+=i)
 *          arr[j] = false;
 *}
 * arr.splice(0,2,false,false)
 * for(let i = n; i<=m; i++){
 *  if(arr[i]) console.log(arr[i])
 *}
 *
 *
 * **/