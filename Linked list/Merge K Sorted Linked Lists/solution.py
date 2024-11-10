import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 定義 __lt__ 方法，讓 ListNode 可以被 heapq 使用
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        # 初始化一個小根堆
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, l)

        # 虛擬節點 (dummy)，用來簡化邏輯
        dummy = ListNode(0)
        current = dummy

        # 每次從堆中彈出最小值節點
        while heap:
            node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next

# 使用範例
# 假設 lists 是包含 k 個已排序鏈表的陣列
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]

# 創建 Solution 物件
solution = Solution()

# 調用 mergeKLists
head = solution.mergeKLists(lists)

# 用來列印鏈表結果的輔助函數
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# 顯示合併後的鏈表
print_linked_list(head)
