N = int(input())
M = int(input())
MAX = float('inf')
board = [[MAX]*N for _ in range(N)]

for _ in range(M):
    a,b,c = map(int,input().split())
    board[a-1][b-1] = min(c,board[a-1][b-1])

for i in range(N):
        board[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j],board[i][k]+board[k][j])

for i in range(N):
    for j in range(N):
        if board[i][j]==MAX:
            print(0,end=" ")
        else:
            print(board[i][j],end=" ")
    print()