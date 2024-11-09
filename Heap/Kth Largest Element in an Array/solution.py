import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 初始化最小堆，存前 k 個元素
        min_heap = nums[:k]
        heapq.heapify(min_heap)


        # 遍歷剩下的元素
        for num in nums[k:] :
            if num > min_heap[0]: # 如果比堆頂大才替換
                heapq.heapreplace(min_heap,num)

        # 堆頂就是第 k 大的元素
        return min_heap[0]
