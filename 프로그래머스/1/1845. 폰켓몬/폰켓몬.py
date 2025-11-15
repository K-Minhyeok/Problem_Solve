def solution(nums):
    opt = len(set(nums))   
    num = len(nums)//2
    
    if opt < num :
        return opt
    else :
        return num
    
        