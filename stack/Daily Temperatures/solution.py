class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n # 初始化結果陣列
        stack = []   # 堆疊用於追蹤索引

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()  # 取出堆疊頂部的索引
                result[prev_index] = i - prev_index  # 計算天數差
            stack.append(i) # 將當前索引放入堆疊

        return result
