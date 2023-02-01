from typing import List

class Solution:
    """
        https://leetcode.com/problems/remove-duplicates-from-sorted-array/

        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
        Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
        Return k after placing the final result in the first k slots of nums.
        Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    
    """ 
    
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 2 and all(nums[0] == n for n in nums):
            return 1
        
        ni = 0
        while ni < len(nums):
            if ni == 0: 
                ni += 1
                continue
            
            curr_n = nums[ni]
            prev_n = nums[(ni - 1) % len(nums)]

            if prev_n == curr_n:
                nums.append(nums.pop(ni))
                
            elif curr_n == max(nums):
                break
            
            else:
                ni += 1
        
        return len(nums[:nums.index(max(nums)) + 1])
    
    
Solution().removeDuplicates([1,1])
Solution().removeDuplicates([1,1,2])
Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])