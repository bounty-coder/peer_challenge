## Given an array of size N containing only 0s, 1s, and 2s
#  sort the array in ascending order.

class Solution:
        # Count the number of zero,one,two and make arr
        # TC- O(2n), SC-O(1)
        def sort012(self,arr,n):
        zero,one,two=0,0,0
        for i in arr:
            if i==0:
                zero+=1
            elif i==1:
                one+=1
            elif i==2:
                two+=1
        arr.clear()
        while zero or one or two:
            if zero>0:
                arr.append(0)
                zero-=1
            elif one>0:
                arr.append(1)
                one-=1
            elif two>0:
                arr.append(2)
                two-=1
        return arr

    #National Dutch FLag
    #TC - O(n) ,SC-O(1)
    def sort012(self,arr,n):
        # code here
        l,m=0,0
        h=n-1
        while m<=h:
            if arr[m]==0:
                arr[l],arr[m]=arr[m],arr[l]
                l+=1
                m+=1
            elif arr[m]==2:
                arr[h],arr[m]=arr[m],arr[h]
                h-=1
            elif arr[m]==1:
                m+=1
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
