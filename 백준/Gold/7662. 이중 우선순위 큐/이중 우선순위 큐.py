import heapq
import sys
def has_num(nums):
    for item in nums:
        if item[1] >0:
            return True
    return False

input= sys.stdin.readline

T = int(input())

for _ in range(T):
    heap_max = []
    heap_min = []
    nums = dict()
    N = int(input())
    for _ in range(N):
        tmp = input().split()
        c,p = tmp[0],int(tmp[1])

        if c == "I":
            if p in nums:
                nums[p] +=1
            else:
                nums[p] =1
                heapq.heappush(heap_max,-p)
                heapq.heappush(heap_min,p)

        if c == "D":
            if has_num(nums.items()):
                if p == 1 :
                    while -heap_max[0] not in nums or nums[-heap_max[0]]<1:
                        t= -heapq.heappop(heap_max)
                        if t in nums:
                            del(nums[t])
                    nums[-heap_max[0]]-=1
                else:
                    while (heap_min[0] not in nums or nums[heap_min[0]]<1):
                        t= heapq.heappop(heap_min)
                        if t in nums:
                            del(nums[t])  
                    nums[heap_min[0]]-=1
                        
                  
    if not has_num(nums.items()):
        print("EMPTY")
    else:
        while heap_min[0] not in nums or nums[heap_min[0]]<1:
            heapq.heappop(heap_min)
        while -heap_max[0] not in nums or nums[-heap_max[0]]<1:
            heapq.heappop(heap_max)
        print(-heap_max[0],heap_min[0])
 