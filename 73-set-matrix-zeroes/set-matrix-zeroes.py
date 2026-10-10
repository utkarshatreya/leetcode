
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

        # Find all zeroes
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Make corresponding rows and columns zero
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0