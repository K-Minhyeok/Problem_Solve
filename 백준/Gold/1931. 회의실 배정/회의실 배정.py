N = int(input())
l = []
cnt = 0
done = -1

for _ in range(N):
    a,b = map(int,input().split())
    l.append((a,b))

l.sort(key=lambda x:(x[1],x[0]))

for start,end in l : 
    if start >=done :
        cnt+=1
        done = end

print(cnt)