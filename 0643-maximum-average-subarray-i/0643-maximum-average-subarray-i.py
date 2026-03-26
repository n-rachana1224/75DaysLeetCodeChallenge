class Solution(object):
    def findMaxAverage(self, nums, k):
        # Initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i]      # add next element
            window_sum -= nums[i-k]    # remove first element of previous window
            max_sum = max(max_sum, window_sum)
        
        return max_sum / float(k)