class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def dfs(r,c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
                
                grid[r][c] = "-1"
                
                dfs(r, c + 1) # right
                dfs(r - 1, c) # up
                dfs(r, c - 1) # left
                dfs(r + 1, c) # down
        
        for r in range (len(grid)):
            for c in range (len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count