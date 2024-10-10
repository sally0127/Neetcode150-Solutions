# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head


        while current :
            next_node = current.next # 儲存下一個節點
            current.next = prev      #反轉當前節點的指向
            prev = current           #更新prev
            current = next_node      #更新prev才能更新current


        return prev # prev 最终会指向新的头节点

        
