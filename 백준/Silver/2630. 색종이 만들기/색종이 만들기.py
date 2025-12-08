def search(ni,nj,n):
    global blue,white
    color = l[ni][nj]     
    for i in range(ni,ni+n):
        for j in range(nj,nj+n):
            if l[i][j] != color:
                search(ni,nj,n//2)
                search(ni,nj+(n//2),n//2)
                search(ni+(n//2),nj,n//2)
                search(ni+(n//2),nj+(n//2),n//2)
                return
    if color == 0:
        white+=1
    else : 
        blue +=1

N = int(input())
l = [[int(x) for x in input().split()] for _ in range(N)]
area_size = N**2
blue = white = 0

search(0,0,N)

print(white)
print(blue)
