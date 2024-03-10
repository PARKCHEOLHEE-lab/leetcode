from typing import List

class Solution:
    """
        https://leetcode.com/problems/trapping-rain-water

        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

        Example 2:
        Input: height = [4,2,0,3,2,5]
        Output: 9


    """
    
    TRAP = 1
    
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        
        return trapped_water
    
    # Memory Limit Exceeded
    def trap_naive(self, height: List[int]) -> int:
        
        row = len(height)
        col = max(height)
        trap_array = [[0 for _ in range(row)] for _ in range(col)]
        
        trapped_water = 0
        
        for hi, h in enumerate(height):
            if h == 0:
                continue
            
            for tr in trap_array[:h]:
                tr[hi] = self.TRAP
            
        for tr in trap_array:
            if sum(tr) <= 1:
                continue

            trapped_water_row = 0
            start_counting = False
            for t in tr:
                if t == 1:
                    if start_counting:
                        trapped_water += trapped_water_row
                        trapped_water_row = 0
                    else:
                        start_counting = True
                elif start_counting:
                    trapped_water_row += 1
        
        return trapped_water
        
    
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    
    Solution().trap_naive(height)