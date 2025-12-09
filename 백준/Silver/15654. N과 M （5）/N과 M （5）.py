N,M = map(int,input().split())
l = [int(x) for x in input().split()]
l.sort()
res=[]
def search(start):
    if len(res) == M:
        print(*res)
        return
    for i in range(N):
        if l[i] in res:
            continue
        res.append(l[i])
        search(i+1)
        res.pop()
    
search(0)