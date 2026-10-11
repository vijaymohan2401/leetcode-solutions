class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for s in strs:
            key=[0]*26
            for ch in s:
                key[ord(ch)-ord('a')]+=1
            key=tuple(key)
            if key not in d:
                d[key]=[]
            d[key].append(s)
        return list(d.values())
       