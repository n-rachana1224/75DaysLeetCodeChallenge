class Solution(object):
    def sequentialDigits(self, low, high):
        digits="1234567890"
        output=[]
        for length in range(2,10):
            for start in range(0,10-length):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    output.append(num)

        return output
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        