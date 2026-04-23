class Solution:
    def kthSmallest(self, root, k):
        stack = []
        
        while True:
            # Go to leftmost node
            while root:
                stack.append(root)
                root = root.left
            
            # Process node
            root = stack.pop()
            k -= 1
            
            if k == 0:
                return root.val
            
            # Move to right subtree
            root = root.right