N = int(input())
nums =[int(x) for x in input().split()]
s = sorted(set(nums))
d = {}

for i in range(len(s)):
    d[s[i]] = i

for i in nums :
    print(d[i],end=" ")