class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    diameter = 0  # 用來追蹤直徑的最大值

    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        
        # 計算左、右子樹的深度
        left_depth = depth(node.left)
        right_depth = depth(node.right)

        # 更新直徑（左右深度之和可能是新直徑）
        diameter = max(diameter, left_depth + right_depth)

        # 回傳該節點的最大深度
        return max(left_depth, right_depth) + 1

    depth(root)
    return diameter
