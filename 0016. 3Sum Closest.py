import itertools
from typing import List

class Solution:
    """
        https://leetcode.com/problems/3sum-closest/description/

        Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

        Return the sum of the three integers.

        You may assume that each input would have exactly one solution.

        Example 1:
            Input: nums = [-1,2,1,-4], target = 1
            Output: 2
            Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

        Example 2:
            Input: nums = [0,0,0], target = 1
            Output: 0
            Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

        Constraints:
            3 <= nums.length <= 500
            -1000 <= nums[i] <= 1000
            -104 <= target <= 104
    """
    
    def threeSumClosestNaive(self, nums: List[int], target: int) -> int:
        closest_sum = float("inf")

        for combination in list(itertools.combinations(nums, 3)):
            current_sum = sum(combination)

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if closest_sum == target:
                return closest_sum 
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        sorted_nums = sorted(nums)
        closest_sum = float("inf")

        for ni in range(len(sorted_nums) - 2):
            left = ni + 1
            right = len(sorted_nums) - 1

            while left < right:
                curr_num = sorted_nums[ni]
                left_num = sorted_nums[left]
                right_num = sorted_nums[right]
                
                current_sum = curr_num + left_num + right_num
                
                current_diff = abs(current_sum - target)
                closest_diff = abs(closest_sum - target)

                if current_diff < closest_diff:
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1

                elif current_sum > target:
                    right -= 1
                
                else:
                    return target

        return closest_sum
    
    
if __name__ == "__main__":
    nums = [786, -884, -587, 209, -708, -736, -231, 567, -252, -32, -612, 881, -662, 180, -481, 296, -631, 835, -234, -977, 194, -498, -398, -777, -214, 935, -675]
    target = -8765
    
    Solution().threeSumClosest(nums=nums, target=target)