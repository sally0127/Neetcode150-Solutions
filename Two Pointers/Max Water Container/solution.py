from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0  #指向數組的最左邊 (0)
        right = len(heights)-1  #指向數組的最右邊 (n-1)
        max_water = 0 # 儲存最大水量

        while left < right :
             # 計算當前的儲水量
            water = min(heights[left], heights[right]) * (right - left)
             # 更新最大水量
            max_water = max(max_water,water)


             # 移動指針
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return max_water
