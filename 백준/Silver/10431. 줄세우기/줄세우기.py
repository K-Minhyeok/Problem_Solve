N = int(input())

l = [[int (x) for x in input().split()]for _ in range(N)]
for k in range(N):
    step = 0
    for i in range(1,21):
        for j in range(i+1,21):
            if l[k][i] > l[k][j]:
                tmp = l[k][i]
                l[k][i] = l[k][j]
                l[k][j] = tmp
                step+=1
    print(k+1,step)
