class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v=[]
        for ch in s:
            if ch=='(':
                v.append(')')
            elif ch=='[':
                v.append(']')
            elif ch=='{':
                v.append('}')
            else:
                if not v or v[-1]!=ch:
                    return False
                v.pop()
        return len(v)==0
        
        