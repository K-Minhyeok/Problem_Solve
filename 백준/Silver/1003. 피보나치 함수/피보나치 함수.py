import sys
input = sys.stdin.readline
zero = [0]*41
one = [0]*41
fib = [0]*41
fib[1]= one[1]=zero[0]=1


T = int(input())
for _ in range(T):
    N = int(input())
    for i in range(2,N+1):
        zero[i]=zero[i-1]+zero[i-2]
        one[i]=one[i-1]+one[i-2]
        fib[i] = fib[i-1]+fib[i-2]

    print(zero[N], one[N])