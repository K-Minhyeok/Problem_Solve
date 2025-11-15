H,W,N,M = map(int,input().split())
a = (H-1) // (N+1) +1
b = (W-1) // (M+1) +1
print(a*b)
