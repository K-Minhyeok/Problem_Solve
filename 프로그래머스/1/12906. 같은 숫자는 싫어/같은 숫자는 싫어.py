def solution(arr):
    stack = []
    for i in range(len(arr)):
        if arr[i] == arr[i-1] and i>0:
            continue
        stack.append(arr[i])
    
    return stack
