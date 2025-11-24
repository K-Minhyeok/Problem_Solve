N = int(input())
M = int(input())
S = input().rstrip()

cur=count=answer=0

while cur < M-1 :
    if S[cur:cur+3] =="IOI":
        cur +=2
        count+=1
        if count ==N:
            answer+=1
            count-=1
    else:
        cur+=1
        count=0


print(answer)
