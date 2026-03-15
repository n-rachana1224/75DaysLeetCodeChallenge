class Solution(object):
    def findDisappearedNumbers(self, nums):
        s = set(nums)
        rnums = []
        n = len(nums)
        for i in range(1, n + 1):
            if i not in s:
                rnums.append(i)            
        return rnums