def solution(citations):
    citations.sort()
    n = len(citations)
    print(citations)
    for i in range(n):
        h = n - i
        print(f"{citations[i]} : { h}")
        if citations[i] >= h:
            return h
    return 0
