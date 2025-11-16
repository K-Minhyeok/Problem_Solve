import heapq

def solution(operations):
    #split 해도 될 듯
    # 모든 operations을 반복
    heap=[]
    for operation in operations:
        # print(operation)
        operation = operation.split(" ")
        if operation[0] == "I":
            val = int(operation[1])
            heapq.heappush(heap,-val)
            # print("hit IIII")
        elif operation[0] == "D":
            val = int(operation[1])
            if val ==1 and heap:     
                # print(heap)
                heapq.heappop(heap)
            elif val ==-1 and heap:
                # print(heap)
                #최솟값 빼기
                heap.sort()
                heap.pop()
    
    if heap:
        heap.sort()
        return [-min(heap),-max(heap),]
    else :
        return [0,0]