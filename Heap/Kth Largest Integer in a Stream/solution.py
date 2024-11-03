import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        # 使用 add 方法初始化最小堆
        for num in nums:
            self.add(num)
        
    def add(self, val: int) -> int:
        # 如果堆的大小小於 k，直接將值加入堆中
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # 如果新元素比堆中的最小元素大，則替換堆頂
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)

        
        # 返回堆頂，即第 k 大的元素
        return self.min_heap[0]
