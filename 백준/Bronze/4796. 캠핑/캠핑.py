import sys
input = sys.stdin.readline

i = 1
while 1:
    L,P,V = map(int,input().split())
    # L = 사용할 기간
    # P = 캠핑강 있을 기간
    # V = 휴가 기간
    
    # 17일 중에서는 8/8/1로 나눠짐
    # 8에서 5일 *2 , 1일
    if L == P == V == 0:
        break
    
    part = V//P
    rest = min(V%P,L)

    total = (part*L) + rest
    print(f"Case {i}: {total}")
    i+=1