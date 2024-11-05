import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Step 1: 初始化最大堆 (將所有重量轉為負數)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)


        # Step 2: 模擬過程
        while len(max_heap) > 1 :
            # 取出最重的兩顆石頭 (最小的負數)
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)


            # 比較兩顆石頭重量
            if first != second :
                # 若不相等，將剩餘的重量重新放入堆中
                heapq.heappush(max_heap,-(first - second))

        # Step 3: 返回結果
        return  -max_heap[0] if max_heap else 0
