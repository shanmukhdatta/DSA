## comment for the problem statement leetcpde 4
## Leetcode 4. Median of Two Sorted Arrays
## Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
## The overall run time complexity should be O(log (m+n)).

class solution:
    def findMedianSortedArrays(self, nums1 : list[int], nums2 : list[int]) -> float:
        A,B = nums1,nums2
        total = len(A)+len(B)
        half = total //2
        if len(A) > len(B):
            A,B = B,A
        
        l,r = 0,len(A) -1
        while True:
            i = (l+r)//2 ## partition of A
            j = half -i -2 ## partition of B

            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i+1] if (i+1) < len(A) else float('inf')
            B_left = B[j] if j >=0 else float('-inf')
            B_right = B[j+1] if (j+1) < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right: ## condition for valid partition
                if total % 2 ==0: ## even number of elements
                    return (max(A_left,B_left)+min(A_right,B_right))/2
                else: ## odd number of elements
                    return min(A_right,B_right)
            elif A_left > B_right: ## partition of A is too large
                r = i-1
            else: ## partition of B is too large
                l = i+1

