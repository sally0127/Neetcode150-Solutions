from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 初始化計數器和結果
        self.count = 0
        self.result = None

        # 定義中序遍歷的遞迴函數
        def inorder(node):
            if not node or self.result is not None: # 當找到結果時提前退出
                return

            # 遍歷左子樹
            inorder(node.left)

            # 處理當前節點
            self.count += 1
            if self.count == k :
                self.result = node.val
                return

            # 遍歷右子樹
            inorder(node.right)

        # 開始中序遍歷
        inorder(root)

        # 回傳找到的結果
        return self.result
