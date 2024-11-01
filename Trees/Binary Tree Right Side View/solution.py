from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        queue = deque([root]) # 初始化佇列，包含根節點
        while queue:
            level_size = len(queue) # 當前層節點數
            for i in range(level_size):
                node = queue.popleft() # 取出當前層的節點

                # 如果是當前層的最後一個節點，將值加入結果
                if i == level_size - 1:
                    result.append(node.val)

                # 依序將左、右子節點加入佇列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return result
