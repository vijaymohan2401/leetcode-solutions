class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        for x in range(1,n+1):
            l=0
            r=n-1
            while l<=r:
                m=l+(r-l)//2
                if nums[m]>=x:
                    r=m-1
                else:
                    l=m+1
            c=n-l
            if c==x:
                return x
        return -1


      