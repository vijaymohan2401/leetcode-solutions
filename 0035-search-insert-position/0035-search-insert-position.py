class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        n=len(nums)
        r=n
        while l<r:
            m=l+(r-l)//2
            if nums[m]<target:
                l=m+1
            else:
                r=m
        return l
       