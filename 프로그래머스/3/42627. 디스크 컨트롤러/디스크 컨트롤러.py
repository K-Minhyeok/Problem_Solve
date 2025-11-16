import heapq

def solution(jobs):
    
    time = 0 #현재 시간이 얼마인가 / 들어온 작업을 열 때 사용
    prev = -1
    total_wait =0
    done = 0
    heap =[]
    
    while done != len(jobs) :
        print(prev,":::::",time)
        for job in jobs :
            if prev < job[0] <= time:
                heapq.heappush(heap,[job[1],job[0]])
                print(f"push{job}")
                            
        if heap:
            #작업
            job = heapq.heappop(heap)
            prev = time
            time +=job[0]
            total_wait +=time - job[1]
            done +=1

        else:
            time+=1
            
            
    return total_wait//len(jobs)