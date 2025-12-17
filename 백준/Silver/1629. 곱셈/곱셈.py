A,B,C = map(int,input().split())

# (a^8)%3 
# = (a^4  * a^4 ) % 3
# = (a^2 * a^2 * a^2* a^2  ) %3
# = 

def get_mod(b):
    if b==1 : 
        return A%C
    else:
        k = get_mod(b//2)
        if b%2 == 0:
            return (k*k)%C
        else:
            return (k*k*A)%C

res = get_mod(B)
print(res)