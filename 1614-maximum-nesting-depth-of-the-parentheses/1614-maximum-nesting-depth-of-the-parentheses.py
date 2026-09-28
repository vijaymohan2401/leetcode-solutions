class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c,mc=0,0
        for i in range(len(s)):
            if s[i]=='(':
                c+=1
            elif s[i]==')':
                c-=1
            else:
                continue
            mc=max(mc,c)
        return mc

        