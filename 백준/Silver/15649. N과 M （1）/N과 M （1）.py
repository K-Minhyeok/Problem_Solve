n,m = map(int, input().split())
result = []

def back_tracking():
    if len(result)== m:
        print(" ".join(map(str,result)))
    else:
        for i in range(1,n+1):
            if i not in result:
                result.append(i)
                back_tracking()
                result.pop()

back_tracking()