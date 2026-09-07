class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        l=1
        r=max(nums)
        while l<=r:
            m=l+(r-l)//2
            t=0
            for num in nums:
                t+=(num+m-1)//m
            if t<=threshold:
                r=m-1
            else:
                l=m+1
        return l


        