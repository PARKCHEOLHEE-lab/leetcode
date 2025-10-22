import random
from typing import List

class PivotPolicy:
    RANDOM = "random"
    START = "start"
    END = "end"
    HALF = "half"


class Solution:
    """
        https://leetcode.com/problems/sort-an-array/
        
        Given an array of integers nums, sort the array in ascending order and return it.

        You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

        Example 1:
            Input: nums = [5,2,3,1]
            Output: [1,2,3,5]
            Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

        Example 2:
            Input: nums = [5,1,1,2,0,0]
            Output: [0,0,1,1,2,5]
            Explanation: Note that the values of nums are not necessarily unique.

        Constraints:
            1 <= nums.length <= 5 * 104
            -5 * 104 <= nums[i] <= 5 * 104
    """
    
    def _quick_sort(self, nums: List[int], pivot_policy: str) -> List[int]:
        
        if len(nums) <= 1:
            return nums
        
        if pivot_policy == PivotPolicy.RANDOM:
            pivot = random.choice(nums)
        elif pivot_policy == PivotPolicy.START:  # Memory Limit Exceeded
            pivot = nums[0]
        elif pivot_policy == PivotPolicy.END:    # Memory Limit Exceeded
            pivot = nums[-1]
        elif pivot_policy == PivotPolicy.HALF:   # Memory Limit Exceeded
            pivot = nums[len(nums) // 2]
        
        left = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        right = [num for num in nums if num > pivot]
        
        return self._quick_sort(left, pivot_policy) + equal + self._quick_sort(right, pivot_policy)
    
    def _quick_sort_inplace(self, nums: List[int], pivot_policy: str, start: int, end: int) -> None:
        
        """
            nums = [0,3,2,1,4,5]
            pivot = 3
        
            [0,3,2,1,4,5]
             L         R
             C
             S         E

            [0,3,2,1,4,5]
               L       R
               C
             S         E

            [0,3,2,1,4,5]
               L       R
                 C
             S         E

            [0,2,3,1,4,5]
                 L     R
                   C
             S         E

            [0,2,1,3,4,5]
                   L   R
                     C
             S         E

            [0,2,1,3,5,4]
                   L R
                     C
             S         E

            [0,2,1,3,5,4]
                   L 
                   R C
             S         E
        """
        
        if start >= end:
            return
        
        if pivot_policy == PivotPolicy.RANDOM:
            pivot = nums[random.randint(start, end)]
        elif pivot_policy == PivotPolicy.START:  # Time Limit Exceeded
            pivot = nums[start]
        elif pivot_policy == PivotPolicy.END:    # Time Limit Exceeded
            pivot = nums[end]
        elif pivot_policy == PivotPolicy.HALF:   # Time Limit Exceeded
            pivot = nums[start + (end - start) // 2]
        
        pointer_left = start
        pointer_current = start
        pointer_right = end
    
        while pointer_current <= pointer_right:
            number = nums[pointer_current]
            
            if pivot > number:
                nums[pointer_left], nums[pointer_current] = nums[pointer_current], nums[pointer_left]
                pointer_left += 1
                pointer_current += 1
                
            elif pivot < number:
                nums[pointer_right], nums[pointer_current] = nums[pointer_current], nums[pointer_right]
                pointer_right -= 1

            else:
                # number == pivot
                pointer_current += 1
        
        self._quick_sort_inplace(nums, pivot_policy, start=start, end=pointer_left - 1)
        self._quick_sort_inplace(nums, pivot_policy, start=pointer_right + 1, end=end)
        
    def sortArray(self, nums: List[int], inplace: bool = True, pivot_policy: str = PivotPolicy.END) -> List[int]:
        
        assert pivot_policy in [PivotPolicy.RANDOM, PivotPolicy.START, PivotPolicy.END, PivotPolicy.HALF]
        
        if not inplace:
            return self._quick_sort(nums, pivot_policy)

        self._quick_sort_inplace(nums, pivot_policy, start=0, end=len(nums) - 1)
        return nums
        