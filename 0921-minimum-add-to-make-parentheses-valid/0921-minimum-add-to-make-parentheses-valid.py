class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        ans=0
        for ch in s:
            if ch=='(':
                c+=1
            else:
                if c>0:
                    c-=1
                else:
                    ans+=1
        return ans+c

        
        