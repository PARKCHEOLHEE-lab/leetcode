from typing import List
    
class Solution:
    """
        https://leetcode.com/problems/container-with-most-water/description/

        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.

        Example 1:
            Input: height = [1,8,6,2,5,4,8,3,7]
            Output: 49
            Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

        Example 2:
            Input: height = [1,1]
            Output: 1
        
        Constraints:
            n == height.length
            2 <= n <= 105
            0 <= height[i] <= 104
    """
    
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        area = 0
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            
            a = h * w
            if area < a:
                area = a
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
    
    def maxAreaNaive(self, height: List[int]) -> int:
        area = 0
        for hi, each_height in enumerate(height):
            for ohi, other_height in enumerate(height[hi + 1:]):

                h = min(each_height, other_height)
                w = ohi + 1
                
                a = h * w
                if area < a:
                    area = a
        
        return area
    
assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49


