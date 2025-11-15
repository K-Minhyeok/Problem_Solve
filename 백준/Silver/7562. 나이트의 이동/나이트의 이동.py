import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
move = [(-2,1) , (-2,-1), (2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

for i in range(N):
    S = int(input())
    night = [int(x) for x in input().split()]
    target = [int(x) for x in input().split()]
    board = [[-1]*S for _ in range(S)]
    queue = deque()


    queue.append((night[0],night[1],0))
    board[night[0]][night[1]] =0

    while queue : 
        x , y ,cnt = queue.popleft()
        if x == target[0] and y == target[1]:
            print(cnt)
            break

        for dx,dy in move:
            if 0<=x+dx<S and 0<=y+dy<S and board[x+dx][y+dy] == -1:
                queue.append((x+dx,y+dy,cnt+1))
                board[x+dx][y+dy] = cnt+1