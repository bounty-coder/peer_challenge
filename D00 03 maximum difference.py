ls=list(map(int,input().split()))
mini=float('inf')
maxi=float('-inf')
for i in range(len(ls)):
    if ls[i]<mini:
        mini=ls[i]
    if ls[i]>maxi:
        maxi=ls[i]

print(maxi-mini)
