class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def ispalindrome(a,b):
           
            while a<b:
                if s[a]!=s[b]:
                    return False
                a+=1
                b-=1
            return True
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                k=i+j-1
                if ispalindrome(j,k):
                    return s[j:k+1]
        return ""

       

        