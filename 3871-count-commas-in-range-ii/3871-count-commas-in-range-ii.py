class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=1000
        res=0
        while c<=n:
            res+=n-c+1
            c*=1000
        return res
     
        