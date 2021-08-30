class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] < 0:
                    count += 1
        return count
        
        
grid = [
        [4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]
