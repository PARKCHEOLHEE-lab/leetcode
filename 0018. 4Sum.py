from typing import List


class Solution:
    """
        https://leetcode.com/problems/4sum/description/
        
        Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

        - 0 <= a, b, c, d < n
        - a, b, c, and d are distinct.
        - nums[a] + nums[b] + nums[c] + nums[d] == target
        
        You may return the answer in any order.

        Example 1:
            Input: nums = [1,0,-1,0,-2,2], target = 0
            Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

        Example 2:
            Input: nums = [2,2,2,2,2], target = 8
            Output: [[2,2,2,2]]

        Constraints:
            1 <= nums.length <= 200
            -109 <= nums[i] <= 109
            -109 <= target <= 109
    """
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums_sorted = sorted(nums)

        quadruplets = set()

        for i in range(len(nums_sorted)):
            for j in range(i + 1, len(nums_sorted)):
                left, right = j + 1, len(nums_sorted) - 1

                while left < right:
                    n1 = nums_sorted[i]
                    n2 = nums_sorted[j]
                    n3 = nums_sorted[left]
                    n4 = nums_sorted[right]

                    sum_n = n1 + n2 + n3 + n4
                    
                    if sum_n == target:
                        quadruplets.add((n1, n2, n3, n4))
                        left += 1
                        right -= 1
                    
                    elif sum_n < target:
                        left += 1
                        
                    elif sum_n > target:
                        right -= 1

        return list(quadruplets)

if __name__ == "__main__":
    Solution().fourSum(nums=[2, 2, 2, 2, 2], target=8)
    Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0)