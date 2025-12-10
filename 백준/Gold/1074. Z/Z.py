N ,r ,C = map(int,input().split())
cnt = 0

def search(i,j,size):
    global cnt
    #r,C 위치면 끝
    if i==r and j ==C :
        print(cnt)
        return
    #i랑j가 없는 곳을 탐색하고 있다면 그냥 그 위치 크기만큼 넘긴다.
    if not ((i<= r < i+size) and (j<=C<j+size)):
        cnt +=size*size
        return
    size = size//2
    search(i,j,size)
    search(i,j+size,size)
    search(i+size,j,size)
    search(i+size,j+size,size)


search(0,0,2**N)

