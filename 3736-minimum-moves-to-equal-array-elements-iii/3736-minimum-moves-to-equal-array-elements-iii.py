class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=max(nums)
        c=0
            
        for num in nums:
            c+=x-num
        return c

        