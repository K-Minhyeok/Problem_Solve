N,G = map(str,input().split())
N = int(N)
p = set()
cnt =0

if G=="Y":
    r = 1
elif G=="F":
    r = 2
elif G=="O":
    r = 3

for _ in range(N):
    p.add(input())

while len(p) > r-1:
    for _ in range(r):
        p.pop()
    cnt+=1
print(cnt)