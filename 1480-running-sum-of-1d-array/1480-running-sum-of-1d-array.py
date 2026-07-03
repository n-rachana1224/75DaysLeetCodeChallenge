class Solution(object):
    def runningSum(self, nums):
        arr=[]
        n=0
        for i in range(len(nums)):
            n=nums[i]+n
            arr.append(n)
        return arr
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        