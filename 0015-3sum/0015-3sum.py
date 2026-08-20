class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        arr=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                if i!=j!=k:
                    s=nums[i]+nums[j]+nums[k]
                    if s==0:
                        arr.append([nums[i],nums[j],nums[k]])
                        j+=1
                        k-=1
                        while j<n and nums[j]==nums[j-1]:
                            j+=1
                        while k>0 and nums[k]==nums[k+1]:
                            k-=1
                    elif s<0:
                        j+=1
                        while j<n and nums[j]==nums[j-1]:
                            j+=1
                    else:
                        k-=1
                        while k>0 and nums[k]==nums[k+1]:
                            k-=1
        return arr
                

                    
                
                    
            
        