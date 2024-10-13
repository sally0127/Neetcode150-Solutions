# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # 虛擬節點，用於處理頭節點被刪除的情況
        dummy.next = head
        fast = slow = dummy


        # 將 fast 向前移動 n+1 步，以便 slow 最後停在倒數第 n 個節點的前一個節點
        for _ in range(n + 1):
            fast = fast.next


        # 同步移動 fast 和 slow，直到 fast 到達鏈結串列的末尾
        while fast:
            fast = fast.next
            slow = slow.next

        # 刪除倒數第 n 個節點
        slow.next = slow.next.next


        return dummy.next   # 返回新的頭節點
