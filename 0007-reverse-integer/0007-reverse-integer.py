class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        s=1
        if x<0:
            s=-1
            x=-x
        while x!=0:
            d=x%10
            rev=rev*10+d
            x/=10
        rev=rev*s
        if rev<-2147483648 or rev>2147483648:
            return 0
        return rev