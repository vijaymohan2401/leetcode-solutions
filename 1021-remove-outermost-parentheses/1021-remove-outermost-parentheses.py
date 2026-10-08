class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        c=0
        for ch in s:
            if ch=='(':
                if c>0:
                    ans+=ch
                c+=1
            else:
                c-=1
                if c>0:
                    ans+=ch
        return ans


        