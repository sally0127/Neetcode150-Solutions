from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,min_val,max_val):
            # 空節點是有效的 BST
            if not node:
                return  True

            # 節點的值不在範圍內，則不是 BST
            if not(min_val < node.val < max_val):
                return False
            # 遞迴檢查左、右子樹
            return (dfs(node.left, min_val, node.val) and
                    dfs(node.right, node.val, max_val))

        # 初始調用範圍為負無窮到正無窮
        return dfs(root, float('-inf'), float('inf'))
