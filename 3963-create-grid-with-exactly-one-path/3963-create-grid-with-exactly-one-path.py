class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        g=[]
        for i in range(m):
            r=[]
            for j in range(n):
                r.append('#')
            g.append(r)
        for i in range(n):
            g[0][i]='.'
        for j in range(m):
            g[j][n-1]='.'
        ans=[]
        for row in g:
            ans.append(''.join(row))
        return ans
        