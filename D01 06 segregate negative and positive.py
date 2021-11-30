## Segregate negative and positive numbers
# used dutch national flag algorithm

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        hi=n-1
        l=0
        while l<=hi:
            if arr[l]<0:
                arr[l],arr[hi]=arr[hi],arr[l]
                hi-=1
            l+=1
        return arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()
