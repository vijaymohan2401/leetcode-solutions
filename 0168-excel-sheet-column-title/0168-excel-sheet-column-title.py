class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res=[]

        while columnNumber>0:
            columnNumber-=1
            rem=columnNumber%26
            res.append(chr(ord('A')+rem))
            columnNumber//=26
        return "".join(reversed(res))