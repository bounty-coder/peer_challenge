## Find duplicates in array in O(n)


def duplicate(ls):
    for i in range(len(ls)):
        if ls[abs(ls[i])]>=0:
            ls[abs(ls[i])]=-ls[abs(ls[i])]
        else:
            print(abs(ls[i]))

#using XOR
#How XOR works??
# A number self XOR will be 0 and any with other will never be 0
def duplicateXOR(ls):
    ans=0
    for i in range(len(ls)):
        ans^=ls[i]
    for i in range(len(ls)):
        ans^=i
    return ans

# #EX:
# FIrst loop
# ans=1^2^3^3

# second loop:
# ans^1^2^3 => 1^2^3^1^2^3^3 => 3
    
ls = list(map(int,input().split()))
print(duplicate(ls))
