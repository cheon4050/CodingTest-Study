function solution(N,M,S){
    let ans = 0;
    for (let i = 0; i < M; i++)
    {
        let k = 0; // k는 IOI의 길이. IOI면 1 , IOIOI면 2
        // O가 나오면 pass
        if (S[i] === 'O')
            continue;
        // s[i] == 'I'일 때
        else
        {
            while (S[i + 1] === 'O' && S[i + 2] === 'I')
            {
                k++;
                if (k === N)
                {
                    k--; // 중복 카운트를 막기 위해 -1 해준다.
                    ans++;
                }
                i += 2; // O를 건너 뛴다.
            }
            k = 0;
        }
    }
    console.log(ans);
}
// solution(1,13,"OOIOIOIOIIOII");
solution(1,13,"OOIOIOIOIIOII");