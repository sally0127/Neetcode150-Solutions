from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

    
        def backtrack(path,used):
            if len(path) == len(nums):
                res.append(path[:])   # 複製當前路徑
                return

            for i in range(len(nums)):
                if not used[i]: # 如果當前數字未被使用
                    used[i] = True  # 標記為已使用
                    path.append(nums[i])  # 加入當前排列
                    backtrack(path,used)    # 遞歸
                    path.pop()    # 回溯，移除當前數字
                    used[i] = False # 標記為未使用

        backtrack([],[False]*len(nums))
        return res
