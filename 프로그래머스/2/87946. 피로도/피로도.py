from itertools import permutations
def solution(k, dungeons):
    maximum=-1
    possible = list(permutations(dungeons, len(dungeons)))
    save = k
    while possible:
        cand = possible.pop()
        count=0
        k =save
        for pair in cand:
            if k >= pair[0] and k>=pair[1]:
                k-=pair[1]
                count+=1
        maximum = max(count,maximum)
    return maximum