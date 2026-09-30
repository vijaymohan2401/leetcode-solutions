class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res={}
        for ch in s:
            if ch in res:
                res[ch]+=1
            else:
                res[ch]=1
        for ch in t:
            if ch in res and res[ch]>0:
                res[ch]-=1
            else:
                return ch 
        