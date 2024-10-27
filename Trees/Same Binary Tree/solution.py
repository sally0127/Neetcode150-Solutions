class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 1. 檢查兩個樹是否都為 None
        if not p and not q:
            return True
        # 2. 檢查只有一個樹為 None
        if not p or not q:
            return False
        # 3. 檢查根節點值是否相同
        if p.val != q.val:
            return False
        # 4. 遞迴比較左右子樹
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 測試代碼
if __name__ == "__main__":
    # 建立二元樹 p 和 q
    rootP = TreeNode(1)
    rootP.left = TreeNode(2)
    rootP.right = TreeNode(3)

    rootQ = TreeNode(1)
    rootQ.left = TreeNode(2)
    rootQ.right = TreeNode(3)

    # 創建解決方案實例
    solution = Solution()
    
    # 執行相同樹的比較
    output = solution.isSameTree(rootP, rootQ)
    print(output)  # 應該返回 True
