class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]

                left = stack[-1] if stack else -1
                right = i

                width = right - left - 1
                maxArea = max(maxArea , width * height)

            stack.append(i)

        while stack:
            height = heights[stack.pop()]

            left = stack[-1] if stack else -1
            right = len(heights)

            width = right - left - 1
            maxArea = max(maxArea , width * height)

        return maxArea