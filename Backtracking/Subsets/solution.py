from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []


        def backtrack(start:int,path:List[int]):
            # 將當前子集加入結果
            res.append(path[:])
            # 遍歷剩下的元素
            for i in range(start,len(nums)):
                # 選擇 nums[i]
                path.append(nums[i])
                # 遞歸生成子集
                backtrack(i + 1,path)
                # 撤銷選擇，回溯
                path.pop()

        # 從空子集開始生成
        backtrack(0,[])
        return res
