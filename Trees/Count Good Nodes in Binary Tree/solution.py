# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max_val):
            if not node:
                return 0

            # 判斷當前節點是否是好節點
            good = 1 if node.val >= max_val else 0


            # 更新最大值
            max_val = max(max_val,node.val)


            # 遞迴到左右子節點，並累加好節點的數量
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)

            return good

        # 開始遞迴並返回結果
        return dfs(root, root.val)
