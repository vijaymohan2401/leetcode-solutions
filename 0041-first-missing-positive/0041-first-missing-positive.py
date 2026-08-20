class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res=sorted(set(nums))
        expected=1
        

        for num in res:
            if num<=0:
                continue
            if num==expected:
                expected+=1
            elif num!=expected:
                return expected
        return expected
        
            
       
      
        
        
     
       


        