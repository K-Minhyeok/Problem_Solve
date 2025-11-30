N = int(input())
col = [False]*N
dia_up = [False]*(2*N+1)
dia_down = [False]*(2*N+1)
cnt=0

# 반복
    # if 현재 row == n : 경우의 수 1개 추가
    # else 
        # Q를 놓음.
            # 그 다음 row에 놓을 수 있는 칸이 있는가?
                # 이걸 현재 row의 i:j 관계로 처리
            # 호출    

def tracking (row):
    global cnt
    if row == N:
        cnt +=1
        return
 
    for i in range(N):
        if col[i] or dia_up[row+i] or dia_down[row-i]:
            continue
        col[i] =dia_up[row+i] = dia_down[row-i] = True
        tracking(row+1)
        col[i] =dia_up[row+i] = dia_down[row-i] = False


tracking(0)
print(cnt)
