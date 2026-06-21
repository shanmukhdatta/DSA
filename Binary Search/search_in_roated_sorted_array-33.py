## comment gives the problem statemnet of the leetcode 33
##Leetcode 33. Search in Rotated Sorted Array
## There is an integer array nums sorted in ascending order (with distinct values).
## Prior to being passed to your function, nums is rotated at an unknown pivot index k (1 <= k <= nums.length). 
## For example, if nums = [0,1,2,4,5,6,7] might become: [4,5,6,7,0,1,2] by rotating it to pivot index 3.
## Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
## You must write an algorithm that runs in O(log n) time.

class solution:
    def search(self, nums : list[int], target : int) -> int:
        l,r = 0, len(nums)-1

        while l<=r:
            m = (l+r) //2
            if nums[m] == target:
                return m
            ## comment tells to chexk why in left sort or right sorted
            ## if in case both half sorted then check in which half target is present
            ## if target is present in sorted half then search in that half
            ## else search in the other half
            if nums[l] <= nums[m]: ## left half is sorted
                if target >= nums[l] and target < nums[m]: ## target is in left half
                    r = m -1
                else: ## target is in right half
                    l = m +1
            else: ## right half is sorted
                if target > nums[m] and target <= nums[r]: ## target is in right half
                    l = m +1
                else: ## target is in left half
                    r = m -1
        return -1