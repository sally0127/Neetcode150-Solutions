from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack (start:int,path:List[int],remaining:int):
            # 如果達成目標，加入結果列表
            if remaining == 0:
                res.append(path[:])
                return

            # 如果剩餘值小於 0，返回
            if remaining < 0:
                return

            # 遍歷數組
            for i in range(start,len(nums)):
                # 選擇當前數字
                path.append(nums[i])
                # 遞歸處理，允許重複選擇，因此索引不變
                backtrack(i,path,remaining - nums[i])
                # 回溯
                path.pop()
        # 開始回溯
        backtrack(0,[],target)
        return res
