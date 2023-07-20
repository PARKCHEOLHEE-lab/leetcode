from typing import List

class Solution:
    """
        https://leetcode.com/problems/remove-element/
    
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
        Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
        Return k after placing the final result in the first k slots of nums.

        Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        if all(n == val for n in nums):
            return 0
        
        val_count = nums.count(val)
        
        ni = 0
        k = 0
        while ni < len(nums):
            num = nums[ni]
            
            if all(n == val for n in nums[-val_count:]):
                break
            
            if num == val:
                nums.append(nums.pop(ni))
                k += 1
            else:
                ni += 1
        
        return len(nums) - val_count
    

print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
print(Solution().removeElement([3,2,2,3], 3))
print(Solution().removeElement([1,2,2,2], 2))
print(Solution().removeElement([2,2,2,2], 2))
print(Solution().removeElement([3,2,2,3], 3))