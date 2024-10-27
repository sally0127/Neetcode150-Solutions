# 定義 isBalanced 函式來判斷樹是否為高度平衡
def isBalanced(root):
    # 定義一個遞迴函式來計算高度，並同時檢查平衡
    def height(node):
        # 如果節點為空，返回高度 0
        if not node:
            return 0
        
        # 計算左子樹的高度
        left_height = height(node.left)
        # 如果左子樹不平衡，直接返回 -1
        if left_height == -1:
            return -1
        
        # 計算右子樹的高度
        right_height = height(node.right)
        # 如果右子樹不平衡，直接返回 -1
        if right_height == -1:
            return -1
        
        # 如果當前節點的左右子樹高度差大於 1，返回 -1 表示不平衡
        if abs(left_height - right_height) > 1:
            return -1
        
        # 如果平衡，返回當前節點的高度
        return max(left_height, right_height) + 1
    
    # 如果 height 函式返回 -1，表示不平衡；否則為平衡
    return height(root) != -1

=====================================================

步驟解釋：

    1.定義高度計算函式 height(node)：
    
    ．若 node 為 None，表示已到達葉節點的下方，返回高度 0。
    
    2.遞迴計算左右子樹高度：
    
      ．呼叫 height(node.left) 計算左子樹的高度。
      
      ．若左子樹不平衡（返回 -1），立即返回 -1，不繼續檢查。
      
      ．呼叫 height(node.right) 計算右子樹高度，並執行相同步驟。
    
    3.檢查當前節點平衡性：
    
      ．若左右子樹高度差大於 1，則返回 -1 表示此節點不平衡。
    
    4.返回當前節點高度：
    
      ．當前節點的高度為 max(left_height, right_height) + 1。
    
    5.主函式 isBalanced(root)：
    
      ．使用 height(root) 檢查根節點的平衡性。
      
      ．若返回 -1，表示不平衡，則返回 False；否則返回 True。
