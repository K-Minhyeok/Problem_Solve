N = int(input())
cur=1 
cnt =1 

while N>cur:
    cur += 6*cnt
    cnt+=1
print(cnt) 