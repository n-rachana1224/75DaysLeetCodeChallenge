class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
        

        """if len(s)!=len(t):
            return False
        return sorted(s)==sorted(t)"""
        