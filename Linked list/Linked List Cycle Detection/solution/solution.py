# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head   # 初始化快慢指針


        while fast and fast.next :
            slow = slow.next    # 慢指針每次移動一個節點
            fast = fast.next.next   # 快指針每次移動兩個節點

            if slow == fast :   # 如果快慢指針相遇，則存在 cycle
                return True

        return False  # 若迴圈結束而未相遇，則無 cycle
