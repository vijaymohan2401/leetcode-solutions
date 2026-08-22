class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        mi=len(grid[0])
        c=0
        for row in grid:
            l=0
            r=mi-1
            while l<=r:
                m=l+(r-l)//2
                if row[m]<0:
                    c+=r-m+1
                    r=m-1
                else:
                    l=m+1
        return c

      