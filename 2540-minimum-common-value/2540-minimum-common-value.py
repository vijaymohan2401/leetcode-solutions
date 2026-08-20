class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        arr=list(set(nums1)&set(nums2))
        if not arr:
            return -1
        arr.sort()
        return arr[0]
        