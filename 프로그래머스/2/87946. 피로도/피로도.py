num = answer = 0
visited =[]

def search(cnt,k,dungeons):
    global answer 
    answer = max(cnt,answer)
    
    for i in range(num):
        if k >=dungeons[i][0] and not visited[i]:
            visited[i] = True
            search(cnt+1,k-dungeons[i][1],dungeons)
            visited[i] = False
    

def solution(k, dungeons):
    global num,visited
    num = len(dungeons)
    visited = [False]*num
    search(0,k,dungeons)
    return answer