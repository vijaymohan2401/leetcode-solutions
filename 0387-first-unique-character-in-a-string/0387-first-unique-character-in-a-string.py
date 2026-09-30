class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res={}
        for ch in s:
            if ch in res:
                res[ch]+=1
            else:
                res[ch]=1
        for i in range(len(s)):
            if res[s[i]]==1:
                return i
        return -1







            

            

        