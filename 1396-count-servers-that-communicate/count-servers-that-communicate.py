
class Solution:
    def countServers(self, grid):
        m = len(grid)
        n = len(grid[0])

        rowCount = [0] * m
        colCount = [0] * n


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowCount[i] += 1
                    colCount[j] += 1

        ans = 0

    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rowCount[i] > 1 or colCount[j] > 1:
                        ans += 1

        return ans
