class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []#this needs to be a stack of tuples, (index, height)

        maxHeight = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                maxHeight = max(maxHeight, (i - index)* height)
                start = index

            stack.append((start, h))


        
        for i, h in stack:
            maxHeight = max(maxHeight, (len(heights) - i) * h)

        return maxHeight