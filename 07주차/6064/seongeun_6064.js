const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n").map(v=>v.split(' ').map(Number));
const T = input.splice(1);
const answer = [];

T.forEach(v=>{
    const [M,N,X,Y] = v;
    const last = lcm(N,M);  // 최소공배수에 종말.
    let x = X;
    let y = Y;
    while(true){
        if(x>last || y>last){  // 종말
            answer.push(-1)
            break;
        }else if(x>y){ //  // x가 더 크면 y를 더해줌.
            y+=N
        }else if(x<y){ //  y가 더 크면 x를 더해줌
            x+=M
        }else{         // x랑 y 가 같다면 그게 정답.
            answer.push(x)
            break;
        }
    }
})

//출력
console.log(answer.join('\n'))


//최대 공약수 구하기.
function gcd(a,b){
    if(b===0) return a;
    return a>b ? gcd(b,a%b) : gcd(a,b%a);
}

//최대 공배수 구하기
function lcm(a,b){
    return (a*b)/gcd(a,b);
}