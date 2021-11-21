#Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.

# Following code shows 
# time complexity- O(nlogn) 

def merge( intervals):
    p=[]
    intervals.sort(key=lambda x:x[0])
    for i in range(len(intervals)):
        a=intervals[i]
        if i==0:
            p.append(a)
        else:
            if a[0]<=p[-1][1]:
                if a[1]>=p[-1][1]:
                    p[-1][1]=a[1]
                else:
                    pass
            else:
                p.append(a)
    return p

arr=[[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))