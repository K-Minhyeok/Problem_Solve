import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    tmp = sys.stdin.readline().strip().split()
    if len(tmp) ==1:
        if tmp[0]=="empty":
            S = set()        
        if tmp[0]=="all":
            S = set([i for i in range(1, 21)])
    else:
        c,p = tmp[0],tmp[1]
        p = int(p)
        if c=="add":
            S.add(p)
        if c=="check":
            if p in S:
                print("1")
            else :
                print("0")
        if c=="remove":
            S.discard(p)
        if c=="toggle":
            if p in S:
                S.discard(p)
            else :
                S.add(p)

        