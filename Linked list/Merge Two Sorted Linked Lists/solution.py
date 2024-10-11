# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # 建立一個虛擬頭節點
        current = dummy     # 用於構建新鏈結串列

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 將剩餘的鏈結串列接到當前節點的尾部
        current.next = list1 if list1 else list2

        return dummy.next   # 返回新的鏈結串列的頭節點
