class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        t=m+n
        i,j=0,0
        curr=0
        prev=0
        for count in range(t//2+1):
            prev=curr
            if i<m and j<n:
                if nums1[i]<=nums2[j]:
                    curr=nums1[i]
                    i+=1
                else:
                    curr=nums2[j]
                    j+=1
            elif i<m:
                curr=nums1[i]
                i+=1
            else:
                curr=nums2[j]
                j+=1
        if t%2==1:
            return curr
        else:
            return (prev+curr)/2.0
      