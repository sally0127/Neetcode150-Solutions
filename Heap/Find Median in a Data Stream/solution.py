import heapq

class MedianFinder:

    def __init__(self):
        # 最大堆 (存放較小的一半，取負數實現最大堆)
        self.low = []
        # 最小堆 (存放較大的一半)
        self.high = []

    def addNum(self, num: int) -> None:
        # Step 1: 插入到最大堆
        heapq.heappush(self.low,-num)
        # Step 2: 將最大堆堆頂移到最小堆
        heapq.heappush(self.high,-heapq.heappop(self.low))
        # Step 3: 平衡兩個堆的大小
        if len(self.low) < len(self.high):
            heapq.heappush(self.low,-heapq.heappop(self.high))
        
    def findMedian(self) -> float:
        # 如果最大堆元素多，返回最大堆堆頂
        if len(self.low) > len(self.high):
            return -self.low[0]
        # 否則返回兩堆堆頂的平均值
        return (-self.low[0] + self.high[0]) / 2
