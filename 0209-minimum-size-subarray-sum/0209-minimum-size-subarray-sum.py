class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l=0
        gl=float("inf")
        s=0
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                
                gl=min(gl,r-l+1)
                s-=nums[l]
                l+=1
            
        if gl==float("inf"):
            return 0
        else:
            return gl

        

        