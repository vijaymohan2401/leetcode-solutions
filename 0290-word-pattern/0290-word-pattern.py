class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        w=s.split()
        if len(pattern)!=len(w):
            return False
        d1={}
        d2={}
        for i in range(len(pattern)):
            p=pattern[i]
            d=w[i]

            if p in d1:
                if d1[p]!=d:
                    return False
            else:
                d1[p]=d
            if d in d2:
                if d2[d]!=p:
                    return False
            else:
                d2[d]=p
        return True
        