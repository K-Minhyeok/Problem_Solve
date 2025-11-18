N = int(input())
T = int(input())

board = [[False]*N for _ in range(N)] 
cnt =0

for _ in range(T):
    a,b= map(int,input().split())
    board[a-1][b-1]= True
    board[b-1][a-1]= True


for i in range(N):
    for j in range(N):
        for k in range(N):
            if board[j][i] and board[i][k]:
                board[j][k]= True

for i in range(1,N):
        if board[0][i]:
            cnt+=1

print(cnt)