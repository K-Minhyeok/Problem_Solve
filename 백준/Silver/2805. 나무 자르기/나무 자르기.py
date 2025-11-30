import sys
input = sys.stdin.readline

N , M = map(int,input().split())
l = [int (x) for x in input().split()]
start , end = 0 , max(l)

while start <= end:
    mid = (start+end)//2
    total = 0
    for i in l:
        if i>mid:
            total +=i - mid
            if total >= M: 
                break

    if total >= M:
        start = mid+1
    else :
        end = mid-1

print(end)