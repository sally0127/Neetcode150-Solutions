# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 從根節點開始遍歷
        current = root
        while current:
            # 如果 p 和 q 都在左子樹
            if p.val < current.val and q.val < current.val:
                current = current.left
            # 如果 p 和 q 都在右子樹
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # 否則，當前節點就是 LCA
            else:
                return current

==================================================================

這題用到了一些經典的 **樹結構與演算法** 的觀念，尤其是針對 **二元搜尋樹（BST）** 的特性做最佳化。我們可以來看看這題中的重要觀念：

1. **二元搜尋樹（Binary Search Tree, BST）特性**：
   - BST 的特性是左子樹的節點值都比根節點小，右子樹的節點值都比根節點大。這種特性讓我們可以在 O(log n) 的時間內查找特定節點或執行範圍查詢，讓整體的運算更加高效。
   - 這題中，我們正是利用 BST 的這個特性，來判斷 `p` 和 `q` 應該在當前節點的左邊還是右邊，從而快速縮小範圍。

2. **遞迴與迭代的選擇**：
   - 這題其實可以用遞迴或迭代來解，不過因為我們只需要找到單一路徑，所以選擇 **迭代**（用 `while` 迴圈）會更節省空間，也避免了遞迴深度太深時可能導致的呼叫堆疊溢出。
   
3. **最低公共祖先（Lowest Common Ancestor, LCA）**：
   - LCA 問題在樹結構中是經典的考題，很多情境下都會用到。例如在檔案系統中找到兩個文件的最近共同目錄等。理解 LCA 也有助於在更複雜的資料結構（如圖結構）中找到相似解法。

4. **分治法的概念**：
   - 雖然這題我們沒有顯式使用「分治法」，但其實是把整棵樹切分為「左右子樹」，然後看 `p` 和 `q` 是否分別在不同子樹中來確定 LCA。分治法的核心精神就是「分而治之」，這題實際上是利用二元搜尋樹的特性來「分」，從而快速「治」。

5. **時間與空間複雜度分析**：
   - 因為利用了 BST 特性，我們可以在平均情況下達成 O(log n) 的時間複雜度。這樣的效率分析對於優化程式碼非常重要。
   - 空間上則是常數空間 O(1)，因為沒有使用額外的遞迴堆疊或其他額外儲存空間。

這些觀念結合起來，不但讓我們能夠有效率地解決這個問題，也為處理其他樹結構問題提供了基礎。
