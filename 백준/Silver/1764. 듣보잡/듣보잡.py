import sys
input = sys.stdin.readline

lis = set()
see = set()
common = []

N,M = map(int,input().split())

for _ in range(N):
    lis.add(input().strip())

for _ in range(M):
    name = input().strip()
    see.add(name)
    if name in lis:
        common.append(name)

print(len(common))
common.sort()
for i in range(len(common)):
    print(common[i])


