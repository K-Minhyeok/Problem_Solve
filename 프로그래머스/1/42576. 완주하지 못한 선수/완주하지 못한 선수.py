def solution(participant, completion):
    stat = dict()
    answer =''
    print()
    for name in participant:
        if name in stat:
            stat[name] = stat[name]+1
        else :    
            stat[name] = 1

    for name in completion:
        stat[name] -=1 

    for name in stat : 
        if stat[name] == 1:
            answer = name
    return answer