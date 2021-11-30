## show all repeated no in list
## brute force approach

def countduplicate(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

ls=list(map(int,input().split()))
print(countduplicate(ls))
