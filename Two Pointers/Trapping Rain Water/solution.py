from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 # 初始化左指針
        right = len(height)-1  # 初始化右指針
        left_max = 0 # 左側最大高度
        right_max = 0 # 右側最大高度
        max_water = 0 # 儲存最大水量

        while left < right :
            if height[left] < height[right]:
                if height[left]>=left_max :
                    left_max = height[left]
                else:
                    max_water += left_max - height[left]
                left += 1

            else:
                 if height[right] >= right_max:
                    right_max = height[right]
                 else:
                    max_water += right_max - height[right]
                 right -= 1
        
        return max_water
