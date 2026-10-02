class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote)>len(magazine):
            return False
        d1={}
        d2={}
        for ch in ransomNote:
            if ch in d1:
                d1[ch]+=1
            else:
                d1[ch]=1
        for ch in magazine:
            if ch in d2:
                d2[ch]+=1
            else:
                d2[ch]=1
        for ch in d1:
            if ch not in d2:
                return False
            if d1[ch]>d2[ch]:
                return False
        return True
            

        