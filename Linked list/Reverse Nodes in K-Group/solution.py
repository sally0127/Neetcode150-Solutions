# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 計算鏈表的總節點數
        def countNodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        # 反轉鏈表中的 k 個節點
        def reverseKNodes(start,k):
            prev,curr = None,start
            for _ in range(k):
                next_node = curr.next
                curr.next =prev
                prev = curr
                curr = next_node
            return prev  # 返回反轉後的新頭節點

        # 主函數，用於按 k 分組反轉
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        total_nodes = countNodes(head)

        while total_nodes >=k:
            group_start = prev_group_end.next
            group_end = group_start


            # 移動到分組的結尾
            for _ in range(k - 1):
                group_end = group_end.next

            # 存儲下一組的起點
            next_group_start = group_end.next

            # 反轉當前的 k 個節點
            new_group_start = reverseKNodes(group_start, k)

            # 將反轉後的分組與前部分連接
            prev_group_end.next = new_group_start
            group_start.next = next_group_start

            # 更新 prev_group_end 到反轉後的結尾
            prev_group_end = group_start
            total_nodes -= k 

        return dummy.next
