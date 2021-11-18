#  An element is leader if it is 
# greater than all the elements to its right side. 
# And the rightmost element is always a leader.

# input 
# [ 15, 17, 12, 8, 9, 4, 2 ]

# output 
# {17, 12, 9, 4, 2}

def leader(ls):
    l=len(ls)
    op=[]
    maxi=float("-inf")
    for i in range(l-1,-1,-1):
        if ls[i]>maxi:
            maxi=ls[i]
            op.insert(0,maxi)
    return op


ls=list(map(int,input().split()))
print(leader(ls))