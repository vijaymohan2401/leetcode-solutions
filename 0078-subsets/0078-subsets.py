class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr=[[]]
        n=len(nums)
        for i in range(n):
            for j in range(len(arr)):
                arr.append(arr[j]+[nums[i]])
        return arr
        