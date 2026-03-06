class Solution(object):
    def checkValidGrid(self, grid):
        n = len(grid)

        pos = [None] * (n*n)
        for i in range(n):
            for j in range(n):
                pos[grid[i][j]] = (i,j)

        if pos[0] != (0,0):
            return False

        for i in range(1, n*n):
            x1,y1 = pos[i-1]
            x2,y2 = pos[i]

            dx = abs(x1-x2)
            dy = abs(y1-y2)

            if not ((dx==2 and dy==1) or (dx==1 and dy==2)):
                return False

        return True
