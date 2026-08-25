class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<2:
            return True
        l=1
        r=num//2
        while l<=r:
            m=l+(r-l)//2
            s=m*m
            if s==num:
                return True
            elif s<num:
                l=m+1
            else:
                r=m-1
        return False
        