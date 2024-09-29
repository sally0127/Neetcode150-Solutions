from typing import List
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 第一步，排序數組
        res = [] # 存放結果
        n = len(nums)

        # 遍歷每個數字
        for i in range(len(nums)-2):
              # 避免重複的三元組
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
        # 初始化兩個指針
            left,right = i+1,n-1
            
            while left < right :
                total = nums[i] + nums[left] +nums[right]

                if total == 0:
                    res.append([nums[i],nums[left],nums[right]])

                    # 跳過重複的 left 和 right
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    

                    # 移動指針
                    left+=1
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    right-=1
                
        return res
