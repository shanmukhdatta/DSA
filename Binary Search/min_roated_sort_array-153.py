# comment gives the problem statememt of leetcode 153
## Leetcode 153. Find Minimum in Rotated Sorted Array
## There is an integer array nums sorted in ascending order (with distinct values).
## Prior to being passed to your function, nums is rotated at an unknown pivot index k (1 <= k <= nums.length). 
## For example, if nums = [0,1,2,4,5,6,7] might become: [4,5,6,7,0,1,2] by rotating it to pivot index 3.
## Return the minimum element of nums.
## You must write an algorithm that runs in O(log n) time.

class solution:
    def findMin(slef, nums : list[int]) -> int:
        # find the pivot element where rotataion occured
        res = nums[0] ## initialize result with first element
        l,r = 0, len(nums)-1

        while l <=r:
            if nums[l] <= nums[r]: ## if left element is less than right element then array is sorted
                res = min(res, nums[l])
                break
            
            m = (l+r) //2
            res = min(res, nums[m])
            if nums[l] <= nums[m]: ## left half is sorted
                l = m +1
            else: ## right half is sorted
                r = m -1
        return res
        
