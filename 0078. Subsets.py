from typing import List


class Solution:
    """
        https://leetcode.com/problems/subsets/
    
        Given an integer array nums of unique elements, return all possible subsets (the power set).

        The solution set must not contain duplicate subsets. Return the solution in any order.

        Example 1:
            Input: nums = [1,2,3]
            Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        Example 2:
            Input: nums = [0]
            Output: [[],[0]]

        Constraints:
            1 <= nums.length <= 10
            -10 <= nums[i] <= 10
            All the numbers of nums are unique.
            
        ----------------

        n => len(nums)
        num_subsets => 2^n

        nums = [1,2,3]
        
               [f,f,f] = [     ]
               [t,f,f] = [1    ]
               [f,t,f] = [  2  ]
               [t,t,f] = [1,2  ]
               [f,f,t] = [    3]
               [t,f,t] = [1,  3]
               [f,t,t] = [  2,3]
               [t,t,t] = [1,2,3]
               
                                  []
                    ┌────────────┴────────────┐
                   [1]                          []
               ┌────┴────┐                ┌────┴────┐
             [1,2]        [1]             [2]         []
           ┌──┴──┐     ┌──┴──┐        ┌──┴──┐     ┌──┴──┐
        [1,2,3] [1,2] [1,3]   [1]    [2,3]   [2]   [3]    []
    """

    def _dfs(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = [(0, [])]

        while stack:
            ni, subset = stack.pop()

            if ni == len(nums):
                res.append(subset)
                continue

            stack.append((ni + 1, subset))
            stack.append((ni + 1, subset + [nums[ni]]))

        return res
    
    def _backtrack(self, nums: List[int]) -> List[List[int]]:
        return

    def subsets(self, nums: List[int], mode: str = "dfs") -> List[List[int]]:
        
        assert mode in ("dfs", "backtrack")
        
        if mode == "dfs":
            return self._dfs(nums)
        elif mode == "backtrack":
            return self._backtrack(nums)
        

if __name__ == "__main__":
    nums = [1,2,3]
    Solution().subsets(nums)