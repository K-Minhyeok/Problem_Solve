from collections import deque

total = input().strip()
b_word = input().strip()
len_b = len(b_word)
stack = []

#stack에 넣는다.
for i in total:
    stack.append(i)
    #폭발 문자열 길이보다 길고
    if len(stack) >= len_b:
        # 지금 append한 것까지 포함해서 폭발 문자열만큼 봤을 때 문자열이랑 같으면 지운다.
        if "".join(stack[-len_b:]) ==b_word:
            del stack[-len_b:]

print("".join(stack) if stack else "FRULA")