# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False    # root 為空，返回 False

        if self.isSameTree(root,subRoot):
            return True     # 如果當前子樹與 subRoot 相同，返回 True

        # 否則，繼續檢查左右子樹
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSameTree(self,p:Optional[TreeNode],q: Optional[TreeNode]):
        # 若兩者皆為空
        if not p and not q :
            return True
        # 若其中一個為空
        if not p or not q:
            return False

        # 值不相等
        if p.val != q.val:
            return False

        # 遞迴檢查左右子樹
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
