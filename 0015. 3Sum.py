from typing import List

class Solution:
    """
        https://leetcode.com/problems/3sum/description/
    
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        Example 1:
            Input: nums = [-1,0,1,2,-1,-4]
            Output: [[-1,-1,2],[-1,0,1]]
            Explanation: 
            nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
            nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
            nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
            The distinct triplets are [-1,0,1] and [-1,-1,2].
            Notice that the order of the output and the order of the triplets does not matter.
            
        Example 2:
            Input: nums = [0,1,1]
            Output: []
            Explanation: The only possible triplet does not sum up to 0.

        Example 3:
            Input: nums = [0,0,0]
            Output: [[0,0,0]]
            Explanation: The only possible triplet sums up to 0.
        
        Constraints:
            3 <= nums.length <= 3000
            -10^5 <= nums[i] <= 10^5
    """

    def threeSumPoor(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations

        triplets = []

        for each_combination in combinations(nums, 3):
            if sum(each_combination) == 0:
                sorted_each_combination = sorted(each_combination)
                if sorted_each_combination not in triplets:
                    triplets.append(sorted_each_combination)
        
        return triplets

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)

        triplets = set()

        for i in range(len(nums_sorted)):
            left, right = i + 1, len(nums_sorted) - 1

            while left < right:
                ni = nums_sorted[i]
                nl = nums_sorted[left]
                nr = nums_sorted[right]
                sum_n = ni + nl + nr
                
                if sum_n == 0:
                    triplets.add((ni, nl, nr))
                    left += 1
                    right -= 1
                
                elif sum_n < 0:
                    left += 1
                    
                elif sum_n > 0:
                    right -= 1

        return list(triplets)