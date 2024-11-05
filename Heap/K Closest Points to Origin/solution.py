import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.k = k
        self.max_heap = []

        for x,y in points:
            # 計算距離的平方，這樣可以避免開根號運算
            distance = -(x**2 + y**2)
            # 將距離和點一起存入最大堆中（取負來模擬最大堆）
            heapq.heappush(self.max_heap,(distance,(x,y)))
            # 保持堆的大小為 k
            if len(self.max_heap) > k :
                heapq.heappop(self.max_heap)

        # 從最大堆中取出 k 個距離最近的點並返回
        return [point for (_, point) in self.max_heap]
