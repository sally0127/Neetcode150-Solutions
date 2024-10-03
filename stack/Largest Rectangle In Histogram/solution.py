class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # 在結束時加一個高度為0的條形，確保有遍歷所有高度沒有遺漏

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] -1 #計算寬度
                max_area = max(max_area,h*w) # 更新最大面積
            stack.append(i)
        return max_area
