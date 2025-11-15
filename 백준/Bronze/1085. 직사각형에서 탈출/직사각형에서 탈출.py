h_x , h_y , w , h = map(int,input().split())

shortest_len = 0

if h_x - 0 < abs(h_x - w) :
    shortest_len = h_x
else :
    shortest_len = abs(h_x - w)


if h_y - 0 < abs(h_y - h) :
    if shortest_len > h_y:
        shortest_len = abs(h_y)

else :
    if shortest_len > abs(h_y - h):
        shortest_len = abs(h_y-h)


print(shortest_len)

