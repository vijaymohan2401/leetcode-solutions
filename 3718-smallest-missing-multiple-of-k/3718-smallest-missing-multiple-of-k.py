class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        i=1
        freq={}
        d=0
        for num in nums:
            freq[num]=freq.get(num,0)+1
        while True:
            d=k*i
            if d not in freq:
                return d
            i+=1
            

        