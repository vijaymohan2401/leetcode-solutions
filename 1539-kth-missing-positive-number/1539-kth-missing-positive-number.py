class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        r=len(arr)
        while l<r:
            m=l+(r-l)//2
            mi=arr[m]-(m+1)
            if mi<k:
                l=m+1
            else:
                r=m
        return l+k

       
                    
        

        