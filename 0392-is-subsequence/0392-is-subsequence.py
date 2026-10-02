class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j=0
        for i in range(len(s)):
            f=False
            while j<len(t):

           
                if s[i]==t[j]:
                    f=True
                    j+=1
                    break
                j+=1
                
                
            
            if f==False:
                return False
        return True




        

        