class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch not in sentence:
                return False
        return True
        