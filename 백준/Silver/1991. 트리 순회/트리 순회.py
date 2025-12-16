from collections import defaultdict
import sys
input = sys.stdin.readline
def pre_trav(node):
    print(node,end="")
    if tree[node][0] !='.':
        pre_trav(tree[node][0])
    
    if tree[node][1] !='.':
        pre_trav(tree[node][1])
    

def in_trav(node):
    if tree[node][0] !='.':
        in_trav(tree[node][0])
    
    print(node,end="")

    if tree[node][1] !='.':
        in_trav(tree[node][1])

def post_trav(node):
    if tree[node][0] !='.':
        post_trav(tree[node][0])
    
    if tree[node][1] !='.':
        post_trav(tree[node][1])

    print(node,end="")

N = int(input())
tree = defaultdict(list)
for i in range(N):
    base,left,right = input().split()
    tree[base].append(left)
    tree[base].append(right)

pre_trav('A')
print()
in_trav('A')
print()
post_trav('A')
