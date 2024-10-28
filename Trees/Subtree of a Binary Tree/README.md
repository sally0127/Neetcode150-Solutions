**Subtree of a Binary Tree**
-
🔗 Link: Subtree of a Binary Tree

💡 Difficulty: Easy

🛠️ Topics: 樹的結構Tree Structure、遞迴遍歷Recursive Traversal、基礎條件Base Conditions、邏輯組合Logical Combination、邊界條件Edge Cases

================================================

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

Example 2:

Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false

Constraints:

．0 <= The number of nodes in both trees <= 100.

．-100 <= root.val, subRoot.val <= 100

===============================================

**UMPIRE Method:**

**Understand**

1.問題理解：

．給定兩棵二元樹 root 和 subRoot，判斷 subRoot 是否為 root 的子樹。

2.條件理解：

．子樹的要求是從 root 中的某個節點開始，subRoot 的結構和節點值與之相同。

．root 可以是自己的子樹，即如果 root 和 subRoot 相同，返回 True。

**Match**

1.方法選擇：使用遞迴和DFS遍歷更為合適。具體思路是遍歷 root 樹的每一個節點，並在每一個節點上開始檢查該節點的子樹是否與 subRoot 相同。

2.對比方法選擇：
    ．雖然 BFS 能夠找到 root 的每一層節點，但它不適合用來檢查是否存在結構完全匹配的子樹，因此不採用BFS。

**Plan**

1.計劃概覽：
    
    ．設置一個主函數 isSubtree(root, subRoot)，在 root 樹上遍歷每個節點。
    
    ．在每個節點上調用一個輔助函數 isSameTree(node1, node2)，檢查從當前節點開始的子樹是否與 subRoot 完全一致。

2.計劃步驟：

    ．如果 root 為空且 subRoot 不為空，返回 False（因為空樹不能包含非空子樹）。
    
    ．若 isSameTree(root, subRoot) 返回 True，則直接返回 True（表示 subRoot 是子樹）。
    
    ．遞迴檢查 root.left 和 root.right 是否包含 subRoot 作為子樹。
    
    ．若左右子樹都不包含，則返回 False。

3.輔助函數 isSameTree(node1, node2)：

    ．如果 node1 和 node2 都為空，則返回 True（說明到達葉節點且結構匹配）。
    
    ．如果只有一個為空，返回 False（說明結構不同）。
    
    ．如果 node1.val 不等於 node2.val，返回 False。
    
    ．遞迴檢查 node1.left 對應 node2.left，node1.right 對應 node2.right，都相同則返回 True。

**Implement**

sees solution.py

**Review**

1.邊界條件：
    
    ．root 為空，直接返回 False。
    
    ．subRoot 為空，即任何樹都包含空子樹，所以返回 True。
    
    ．root 和 subRoot 都為空，返回 True。

2.測試案例：
    
    ．標準案例：root 和 subRoot 有完全匹配的子樹。
    
    ．邊界案例：root 或 subRoot 為空的情況。
    
    ．負案例：root 不包含 subRoot，應返回 False。
    
    ．邊緣情況：root 和 subRoot 只有單個節點，且匹配。

**Evaluate**

1.時間複雜度：O(N * M)，其中 N 是 root 的節點數，M 是 subRoot 的節點數。

    ．在最差情況下，遍歷 root 中的每個節點，對每個節點調用 isSameTree 比較兩棵樹，導致複雜度為 O(N * M)。

2.空間複雜度：O(H)，其中 H 是 root 樹的高度，儲存遞迴調用棧的深度。

