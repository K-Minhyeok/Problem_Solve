N , P = map(int,input().split())
l = []
num =0
for _ in range(N):
    val = int(input())
    if val <= P:
        l.append(val)

for i in range(len(l)-1,-1,-1):
    num += P//l[i]
    P=P%l[i]

print(num)