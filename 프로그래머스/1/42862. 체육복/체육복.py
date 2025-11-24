def solution(n, lost, reserve):
    answer = 0
    lo = sorted(set(lost))
    re = sorted(set(reserve))
    
    for r in re[:]:
        if r in lo:
            re.remove(r)
            lo.remove(r)
    
    for r in re:
        if r-1 in lo:
            lo.remove(r-1)
            print(f"{r} to {r-1}")
        elif r+1 in lo:
            lo.remove(r+1)
            print(f"{r} to {r+1}")

    return n-len(lo)