class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        for i in range(1,n):
            if n%i==0:
                p=s[:i]
                r=""
                for j in range(n//i):
                    r+=p
                if r==s:
                    return True
        return False

        