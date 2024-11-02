from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf') # 初始化為負無窮


        def dfs(node):
            if not node:
                return 0

            # 遞迴計算左子樹和右子樹的最大路徑和，若小於 0 則不加入
            left_max = max(dfs(node.left),0)
            right_max = max(dfs(node.right),0)


            # 當前路徑和（包括當前節點和其左右最大子路徑）
            current_path_sum = node.val + left_max + right_max


            # 更新全局最大和
            self.max_sum = max(self.max_sum, current_path_sum)

            # 返回節點的最大貢獻值
            return node.val + max(left_max, right_max)

        #開始DFS
        dfs(root)

        return self.max_sum  
