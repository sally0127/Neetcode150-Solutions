# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root :
            return result

        queue = deque([root]) # 初始化佇列，放入根節點

        while queue:
            level_size = len(queue) # 當前層的節點數
            level = [] # 儲存當前層的值

            for _ in range(level_size):
                node = queue.popleft() # 取出當前層的節點
                level.append(node.val)  # 加入當前節點的值

                # 將下一層節點加入佇列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level) # 當前層的節點值儲存到結果中

        return result
