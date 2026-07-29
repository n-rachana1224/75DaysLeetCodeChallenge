class Solution(object):
    def moveZeroes(self, nums):
        z=[]
        n=[]
        for num in nums:
            if num == 0:
                z.append(num)
            else:
                n.append(num)
        nums[:] = n + z

         
                

        