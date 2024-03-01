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
    
    BFS = "BFS"
    DFS = "DFS"
    
    def __init__(self, mode: str = "BFS") -> None:
        assert mode in (self.BFS, self.DFS)
        self.mode = mode
        self.num_islands = 0

    def visit_island_bfs(self, grid: List[List[str]], r: int, c: int, visited: List[List[bool]]) -> None:
        queue = deque([(r, c)])
        while queue:
            ri, ci = queue.popleft()
            
            if 0 <= ri < len(grid) and 0 <= ci < len(grid[0]) and visited[ri][ci] is False and grid[ri][ci] == self.LAND:
                for dr, dc in self.DIRECTIONS:
                    queue.append((ri + dr, ci + dc))

                visited[ri][ci] = True    

    def visit_island_dfs(self, grid: List[List[str]], r: int, c: int, visited: List[List[bool]]) -> None:
        visited[r][c] = True
        
        for dr, dc in self.DIRECTIONS:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and visited[nr][nc] is False and grid[nr][nc] == self.LAND:
                self.visit_island_dfs(grid, nr, nc, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return self.num_islands
        
        row_num = len(grid)
        col_num = len(grid[0])
        
        visited = [[False] * col_num for _ in range(row_num)]
        
        for r in range(row_num):
            for c in range(col_num):
                if grid[r][c] == self.LAND and visited[r][c] is False:
                    if self.mode == self.BFS:
                        self.visit_island_bfs(grid, r, c, visited)
                    elif self.mode == self.DFS:
                        self.visit_island_dfs(grid, r, c, visited)

                    self.num_islands += 1

        return self.num_islands
