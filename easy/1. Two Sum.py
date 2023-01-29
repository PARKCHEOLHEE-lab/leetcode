from typing import List

class Solution:
    """
        https://leetcode.com/problems/two-sum/

        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        answer = []        
        for ni, num in enumerate(nums):
            other_nums = nums[:ni] + [None] + nums[ni + 1:]
            
            for oni, other_num in enumerate(other_nums):
                if other_num is None:
                    continue
                
                is_break_needed = num + other_num == target
                
                if is_break_needed:
                    break
                
            if is_break_needed:
                answer.extend([ni, oni])
                break
            
        return answer
    

# print(Solution().twoSum(nums=[2,7,11,15], target=9))
# print(Solution().twoSum(nums=[3,2,4], target=6))
# print(Solution().twoSum(nums=[3,3], target=6))
# print(Solution().twoSum(nums=[3,2,3], target=6))
print(Solution().twoSum(nums=[0,4,3,0], target=0))