class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total=numBottles
        while(numBottles>=numExchange):
            numBottles=numBottles-numExchange+1
            total+=1
        return total
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        