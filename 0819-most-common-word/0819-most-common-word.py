class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        w=re.findall(r"[a-z]+",paragraph.lower())
        banned=set(banned)
        d={}
        for word in w:
            if word not in banned:
                d[word]=d.get(word,0)+1
        return max(d,key=d.get)
       
        