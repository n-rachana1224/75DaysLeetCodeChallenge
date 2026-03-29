class Solution(object):
    def isValid(self, s):
        a=[]
        mapping = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in mapping:
                top = a.pop() if a else '#'
                if mapping[c] != top:
                    return False
            else:
                a.append(c)
        return not a
       
        