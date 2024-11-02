from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # 根節點是前序遍歷的第一個元素
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 找到根節點在中序遍歷中的位置
        root_index = inorder.index(root_val)


        # 左子樹和右子樹的中序遍歷部分
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index + 1 :]

        # 前序遍歷中，根節點後的元素中，左子樹的大小為 len(inorder_left)
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        # 遞迴建立左子樹和右子樹
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
