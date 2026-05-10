class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        # Append a 0 to ensure all bars are popped at the end
        heights.append(0) 
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # If stack empty, width is i, else width is between i and new top
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
    
        heights.pop() # Restore original
        return max_area

        