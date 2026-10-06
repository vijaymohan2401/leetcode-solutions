class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l={}
        for i in range(len(s)):
            l[s[i]]=i

        st=[]

        u=set()
        for i in range(len(s)):
            ch=s[i]
            if ch in u:
                continue
            while st and st[-1]>ch and l[st[-1]]>i:
                u.remove(st.pop())
            st.append(ch)
            u.add(ch)
        return ''.join(st)