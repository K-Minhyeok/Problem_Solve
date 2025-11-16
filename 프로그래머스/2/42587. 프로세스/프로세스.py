def solution(priorities, location):
    # circular Queue로 구현
    # 현재 뽑힌 애의 priority == max(priorities) 판단
    # 맞음 && location번째 애가 아님
        # done ++
    # else 
        # return done 
        
    queue = priorities.copy()
    done = 0
    idx = 0
    size = len(priorities)  
    while(done < size):
        cir_idx = idx%size
        print(f'==== {cir_idx}번째 인덱스 접근 ====')
        print(f'{priorities[cir_idx]}와 {max(queue)}비교')        
        if priorities[cir_idx] == max(queue):
            print("hit same")
            done +=1
            if cir_idx == location:
                return done
            else :
                queue.remove(max(queue))
            
        idx+=1
        print(f"{done} 계속")
    
