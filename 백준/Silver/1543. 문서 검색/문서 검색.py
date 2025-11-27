word = input().strip()
find = input().strip()

l = len(find)
cnt=0
i=0
while i < len(word)-l+1:
    # print(f"checking {word[i:i+l]}, i is {i}")
    if word[i:i+l] == find:
        # print("hit")
        cnt+=1
        i+=l
    else:
        i+=1
print(cnt)