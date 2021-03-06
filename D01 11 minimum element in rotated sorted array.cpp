/*
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array will not contain duplicates.

*/

int Solution::findMin(const vector<int> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    int n=A.size();
    int low=0,high=n-1;
    int mid=low+(high-low)/2;
    while(low<=high){
        mid=low+(high-low)/2;
        if((mid>0&&A[mid-1]>A[mid]))
         return A[mid];
        if(mid<n-1&&A[mid]>A[mid+1])
         return A[mid+1];
        if(A[mid]<A[n-1]) high=mid-1;
        else low=mid+1;
    }
    return A[0];
}
