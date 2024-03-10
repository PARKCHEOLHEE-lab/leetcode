from typing import List, Union


class Mode:
    
    NAIVE = "NAIVE"
    ITERATIVE = "ITER"
    TWO_POINTERS = "POINTERS"
    MODES = [NAIVE, ITERATIVE, TWO_POINTERS]
    

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

    def __init__(
        self, 
        mode: Union[
            Mode.NAIVE, 
            Mode.ITERATIVE, 
            Mode.TWO_POINTERS
        ] = Mode.TWO_POINTERS
    ) -> None:
        
        if not mode in Mode.MODES:
            ValueError(f"Incorrect mode is given. `mode`: {mode}")
        
        self.mode = mode
        self.trapped_water = 0
    
    # Runtime 103 ms
    def _trap_two_pointers(self, height: List[int]) -> int:
        li = 0
        ri = len(height) - 1
        
        l_max = height[li]
        r_max = height[ri]
        
        while li != ri:
            if l_max <= r_max:
                li += 1
                l_max = max(l_max, height[li])
                self.trapped_water += l_max - height[li]
            
            else:
                ri -= 1
                r_max = max(r_max, height[ri])
                self.trapped_water += r_max - height[ri]
        
        return self.trapped_water
    
    # Runtime 9837 ms
    def _trap_iterative(self, height: List[int]) -> int:
        for hi in range(len(height)):
            l_max = 0 if hi == 0 else max(height[:hi])
            r_max = 0 if hi == len(height) - 1 else max(height[hi + 1:])
            
            self.trapped_water += max(min(l_max, r_max) - height[hi], 0)

        return self.trapped_water
    
    # Memory Limit Exceeded
    def _trap_naive(self, height: List[int]) -> int:
        
        row = len(height)
        col = max(height)
        trap_array = [[0 for _ in range(row)] for _ in range(col)]
        
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
                        self.trapped_water += trapped_water_row
                        trapped_water_row = 0
                    else:
                        start_counting = True
                elif start_counting:
                    trapped_water_row += 1
        
        return self.trapped_water
    
    def trap(self, height: List[int]) -> int:
        if self.mode == Mode.NAIVE:
            return self._trap_naive(height)
        elif self.mode == Mode.ITERATIVE:
            return self._trap_iterative(height)
        elif self.mode == Mode.TWO_POINTERS:       
            return self._trap_two_pointers(height)
        
    
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution(mode=Mode.TWO_POINTERS).trap(height))

    height = [4,2,0,3,2,5]
    print(Solution(mode=Mode.TWO_POINTERS).trap(height))

    height = [5,5,1,7,1,1,5,2,7,6]
    print(Solution(mode=Mode.TWO_POINTERS).trap(height))