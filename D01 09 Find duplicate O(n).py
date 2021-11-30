## Find duplicates in array in O(n)


def duplicate(ls):
    for i in range(len(ls)):
        if ls[abs(ls[i])]>=0:
            ls[abs(ls[i])]=-ls[abs(ls[i])]
        else:
            print(abs(ls[i]))


ls = list(map(int,input().split()))
print(duplicate(ls))
