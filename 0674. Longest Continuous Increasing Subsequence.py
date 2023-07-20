from typing import List

class Solution:
    """
        https://leetcode.com/problems/longest-continuous-increasing-subsequence/
        Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
        A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
    """
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        subsequences_length = []
        subsequence = []

        ni = 0
        while ni < len(nums):
            num = nums[ni] 
            if ni == 0:
                subsequence.append(num)
                ni += 1
                continue
            
            if num <= subsequence[-1]:
                subsequences_length.append(len(subsequence))
                subsequence = [num]
            
            else:
                subsequence.append(num)
                
            if ni == len(nums) - 1:
                subsequences_length.append(len(subsequence))

            ni += 1
            
        if len(subsequences_length) == 0:
            max_subsequence_length = len(subsequence) 
        
        else:
            max_subsequence_length = max(subsequences_length)
        
        return max_subsequence_length
    
    
print(Solution().findLengthOfLCIS([1,3,5,4,2,3,4,5]))
print(Solution().findLengthOfLCIS([1,3,5,7]))
print(Solution().findLengthOfLCIS([1,3,5,4,2,3,4,5]))
print(Solution().findLengthOfLCIS([1,3,5,4,7]))
print(Solution().findLengthOfLCIS([2,2,2,2,2]))