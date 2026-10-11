class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        ans=0
        for c in d.values():
            ans+=(c//2)*2
        if ans<len(s):
            ans+=1
        return ans


        
        
