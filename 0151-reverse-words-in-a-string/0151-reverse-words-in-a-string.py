class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        w=s.split()
        w.reverse()
        return " ".join(w)