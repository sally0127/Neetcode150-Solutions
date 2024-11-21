class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,path):
            # 將當前 path 添加到結果中
            result.append(path[:])
            # 遍歷數組
            for i in range (start,len(nums)):
                # 跳過重複的元素
                if i > start and nums[i] == nums[i-1]:
                    continue
                # 選擇當前元素並進一步探索
                path.append(nums[i])
                backtrack( i +1 ,path)
                # 回溯，移除最後添加的元素
                path.pop()
        # 初始化
        nums.sort() # 排序以方便處理重複
        result = []
        backtrack(0,[])
        return result
