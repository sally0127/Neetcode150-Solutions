# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 基礎情況：如果節點是空的，回傳 None
        if root is None:
            return None

        # 遞迴反轉左右子樹
        left = self. invertTree(root.left)
        right = self.invertTree(root.right)

        # 將左右子樹對調
        root.left,root.right = right,left

        # 回傳根節點
        return root
