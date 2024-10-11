# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 步驟1：找出中點
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        # 步驟2：反轉後半段
        prev,curr = None,slow.next
        slow.next = None     # 將前半部分的結尾指向None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 步驟3：合併兩部分
        first,second = head,prev
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
