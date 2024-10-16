class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)  # 用來簡化返回結果的處理
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # 計算當前位數的和
        sum = val1 + val2 + carry
        carry = sum // 10  # 計算新的進位
        current.next = ListNode(sum % 10)  # 創建新節點
        current = current.next  # 移動指針

        # 移動到下一個節點
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next  # 返回結果鏈結串列的頭部

