
word = input().upper()
word_l = list(set(word))
cnt =[]

for i in word_l:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt))!=1:
    print("?")
else:
    print(word_l[cnt.index(max(cnt))])