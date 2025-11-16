def solution(prices):
    # 하나를 pop
    # 안에 있는 것들을 순회한다.
    # 자신보다 작은 값이 나올 때까지 count 증가
    num = len(prices)
    answer = []

    for i in range(num):
        price = prices[i]
        count = 0
        idx = i+1
        while idx < num:
            count +=1
            if price > prices[idx]:
                break
            idx +=1 
        answer.append(count)        
    
    return answer