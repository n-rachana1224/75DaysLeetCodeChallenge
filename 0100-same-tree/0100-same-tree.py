# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) :
        # Case 1: both nodes are None
        if not p and not q:
            return True
        
        # Case 2: one is None
        if not p or not q:
            return False
        
        # Case 3: values are different
        if p.val != q.val:
            return False
        
        # Case 4: check left and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)