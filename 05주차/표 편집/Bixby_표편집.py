def solution(n, k, cmds):
    table=['O']*n
    up=[-1]+[i for i in range(n-1)]
    down=[i for i in range(1,n)]+[-1]
    recycleBin=[]

    for cmd in cmds:
        c=cmd.split()

        if c[0]=="U":
            for _ in range(int(c[1])):
                k=up[k]
        elif c[0]=="D":
            for _ in range(int(c[1])):
                k=down[k]

        elif c[0]=="C":
            if up[k]!=-1:
                down[up[k]]=down[up[k]]
            if down[k]!=-1:
                up[down[k]]=up[k]
            table[k]='X'
            recycleBin.append(k)
            k=down[k] if down[k]!=-1 else up[k]

        elif c[0]=="Z":
            r=recycleBin.pop()
            if up[r]!=-1:
                down[up[r]]=r
            if down[r]!=-1:
                up[down[r]]=r
            table[r]='O'
    return ''.join(table)


cmd=["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(8,2,cmd))