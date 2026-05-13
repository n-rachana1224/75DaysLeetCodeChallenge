class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # If the middle element is smaller than the next one, 
            # we are on an upward slope, so the peak is to the right.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # We are on a downward slope, so the peak is to the left (including mid)
                right = mid
        
        return left
