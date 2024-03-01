from collections import deque
from typing import List

class Solution:
    """
        https://leetcode.com/problems/number-of-islands/
        
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
        
        You may assume all four edges of the grid are all surrounded by water.
 
        Example 1:
            Input: grid = [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ]
            Output: 1

        Example 2:
            Input: grid = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
            Output: 3
    
    """

    WATER = "0"
    LAND = "1"
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def visit_island(self, grid: List[List[str]], r: int, c: int, visited: List[List[bool]]) -> None:
        queue = deque([(r, c)])
        while queue:
            ri, ci = queue.popleft()
            
            if 0 <= ri < len(grid) and 0 <= ci < len(grid[0]) and visited[ri][ci] is False and grid[ri][ci] == self.LAND:
                for dr, dc in self.DIRECTIONS:
                    queue.append((ri + dr, ci + dc))

                visited[ri][ci] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        
        if len(grid) == 0:
            return num_islands

        row_num = len(grid)
        col_num = len(grid[0])

        visited = [[False] * col_num for _ in range(row_num)]

        for r in range(row_num):
            for c in range(col_num):
                if grid[r][c] == self.LAND and not visited[r][c]:
                    self.visit_island(grid, r, c, visited)
                    num_islands += 1

        return num_islands
    
    
if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1", "1", "1", "1", "0"], 
        ["1", "1", "0", "1", "0"], 
        ["1", "1", "0", "0", "0"], 
        ["0", "0", "0", "0", "0"]
    ]
    
    grid = [
        ["1","1","0","0","0"], 
        ["1","1","0","0","0"], 
        ["0","0","1","0","0"], 
        ["0","0","0","1","1"]
    ]
    
    print(s.numIslands(grid))

