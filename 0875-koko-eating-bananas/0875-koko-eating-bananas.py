class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l=1
        hi=max(piles)
        while l<=hi:
            m=l+(hi-l)//2
            t=0
            for i in range(len(piles)):
                t+=(piles[i]+m-1)//m
            if t<=h:
                hi=m-1
            else:
                l=m+1
        return l



        
        