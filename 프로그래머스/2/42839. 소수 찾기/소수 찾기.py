import itertools

def is_prime_number(number):
    if number ==1 or number==0:
        return False
    if number <=2:
            return True
    
    for i in range(2,number):
        if number%i ==0:
            return False
    
    return True

def solution(numbers):
    pair = []
    

    #1) 각 문자들로 만들 수 있는 Permutation을 구하여 숫자로 변환한다.
    for i in range(1, len(numbers) + 1):
        perms = list(itertools.permutations(numbers, i))
        for perm in perms:
            pair.append(int(''.join(map(str, perm))))
    
    #2) 변환되어 저장된 값들의 중복을 없앤다.
    pair = list(set(pair))
    
    answer = 0

    #3) 저장된 값들이 소수인지 판단한다.
    for num in pair:
        if is_prime_number(num):
            print(f"{num} hit")
            answer+=1
    return answer