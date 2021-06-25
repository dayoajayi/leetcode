class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def dfs(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1":

                grid[row][col] = "-1"
                
                dfs(row, col - 1)
                dfs(row + 1, col)
                dfs(row, col + 1)
                dfs(row - 1, col)
        
        for i in range(len(grid)): #rows
            for j in range(len(grid[0])): #cols
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
                    
                    
    
            
                
                
                
                