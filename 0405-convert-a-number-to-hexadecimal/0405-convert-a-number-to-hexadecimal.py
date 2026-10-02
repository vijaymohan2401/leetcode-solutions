class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        c="0123456789abcdef"
        ans=""
        if num<0:
            num=num&0xffffffff
        while num>0:
            rem=num%16
            ans=c[rem]+ans
            num//=16
        return ans

        