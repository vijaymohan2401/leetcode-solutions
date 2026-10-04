class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        h=0
        for c in s:
            if c=='(':
                l+=1
                h+=1
            elif c==')':
                l-=1
                h-=1
            else:
                l-=1
                h+=1
            if l<0:
                l=0
            if h<0:
                return False
        return l==0
                
            
        