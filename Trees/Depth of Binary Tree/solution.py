1.遞迴
-

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root):
    # 如果樹是空的，深度就是 0
    if root is None:
        return 0
    
    # 遞迴計算左右子樹的深度
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # 當前節點的深度 = 左右子樹的最大深度 + 1
    return 1 + max(left_depth, right_depth)

===================================================

2.「廣度優先搜尋」（BFS）

from collections import deque

def maxDepth(root):
    if root is None:
        return 0
    
    # 初始化佇列，把根節點放進去
    queue = deque([root])
    depth = 0
    
    while queue:
        # 每次處理佇列中的所有節點（即同一層的節點）
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()  # 取出當前層的一個節點
            
            # 如果這個節點有子節點，把它們加入佇列
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # 每處理完一層，深度加一
        depth += 1
    
    return depth



