class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==0:
                    continue
                p=p+4
                if i>0:
                    p=p-grid[i-1][j]
                if j>0:
                    p=p-grid[i][j-1]
                if i<len(grid)-1:
                    p=p-grid[i+1][j]
                if j<len(grid[i])-1:
                    p=p-grid[i][j+1]
        return p
