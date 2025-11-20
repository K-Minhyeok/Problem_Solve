from collections import defaultdict
import sys
input = sys.stdin.readline
d = defaultdict(str)

N,M = map(int,input().split())
for _ in range(N):
    pair = input().split()
    url,pswd = pair[0],pair[1]
    d[url]=pswd

for _ in range(M):
    url = input().strip()
    print(d[url])
