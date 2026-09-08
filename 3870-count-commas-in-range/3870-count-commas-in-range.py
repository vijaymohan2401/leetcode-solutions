class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        if n<1000:
            return 0
        else:
           n-=1000
        return n+1


        