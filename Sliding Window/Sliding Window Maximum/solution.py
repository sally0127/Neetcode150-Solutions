from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        deq = deque()   # 存儲元素的索引
        max_values = [] # 存儲每個窗口的最大值

        for i in range(len(nums)):
            # 移除不在窗口內的索引
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            # 移除所有小於當前元素的索引
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            deq.append(i)  # 添加當前元素的索引

            # 當窗口大小達到 k 時，添加當前窗口的最大值
            if i >= k - 1:
                max_values.append(nums[deq[0]])

        return max_values
