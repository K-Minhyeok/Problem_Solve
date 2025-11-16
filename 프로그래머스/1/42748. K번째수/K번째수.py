def solution(array, commands):
    answer = []
    for command in commands:
        to_sort = array[command[0]-1:command[1]]
        to_sort.sort()
        answer.append(to_sort[command[2]-1])
    
    return answer