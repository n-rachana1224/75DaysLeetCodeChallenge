class Solution(object):
    def defangIPaddr(self, address):
        res=''
        for i in address:
            if i==".":
                res=res+"[.]"
            else:
                res= res+i
        return res
        """
        :type address: str
        :rtype: str
        """
        