**Kth Smallest Integer in BST**
-

🔗 Link: Kth Smallest Integer in BST

💡 Difficulty: Medium

🛠️ Topics: 二元搜尋樹 (Binary Search Tree, BST)、中序遍歷 (In-order Traversal)、遞迴 (Recursion)、計數 (Counting)、提前退出 (Early Exit)

==============================================

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

．The left subtree of every node contains only nodes with keys less than the node's key.

．The right subtree of every node contains only nodes with keys greater than the node's key.

．Both the left and right subtrees are also binary search trees.

Example 1:

Input: root = [2,1,3], k = 1
Output: 1

Example 2:

Input: root = [4,3,5,2,null], k = 4
Output: 5

Constraints:

．1 <= k <= The number of nodes in the tree <= 1000.

．0 <= Node.val <= 1000

========================================================

**UMPIRE Method**

**Understand**

1.問題陳述：給定一個二元搜尋樹（BST）和一個正整數 k，回傳 BST 中第 k 小的值。

2.條件：

    ．BST 的每個節點的左子樹節點值小於根節點值，右子樹節點值大於根節點值。
    
    ．k 是從 1 開始計數的，且 k 一定在有效的節點範圍內。

**Match**

方法選擇：使用 DFS 中序遍歷。因為 BST 的中序遍歷會自動將節點值按大小排序。

**Plan**

1.初始化：進行 DFS 中序遍歷，並使用一個計數器 count 來追蹤我們目前到第幾個最小值。

2.遞迴遍歷：中序遍歷按左子樹 -> 根節點 -> 右子樹的順序。

3.檢查條件：當 count 等於 k 時，表示我們已找到第 k 小的值，返回該節點的值。

4.結束條件：當 count 達到 k 時停止遍歷。

**Implement**

see solution.py

**Review**

1.邏輯確認：這段程式碼通過中序遍歷以遞增順序遍歷所有節點，且當 count 等於 k 時返回當前節點值。

2.特殊情況檢查：假設 BST 具有至少 k 個節點，因為題目保證 k 是有效的。

**Evaluate**

時間複雜度：最壞情況下為 O(N)，因為可能需要遍歷整棵樹，尤其是當第 k 小的元素接近樹葉節點時。

空間複雜度：遞迴調用的空間複雜度為 O(H)，其中 H 是樹的高度，最壞情況下 H≈N（不平衡樹），而最佳情況下為 O(logN)（平衡樹）。

