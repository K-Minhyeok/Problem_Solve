import sys

input = sys.stdin.readline

N,M = map(int,input().split())
name = dict()
idx = dict()

for i in range(1,N+1):
    tmp_n = input().strip()
    idx[i] = tmp_n
    name[tmp_n] = i

for i in range(M):
    x = input().strip()
    if x.isdigit():
        x=int(x)
        print(idx[x])
    else:
        print(name[x])

