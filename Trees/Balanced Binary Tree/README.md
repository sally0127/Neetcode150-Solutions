**Balanced Binary Tree**
-
🔗 Link: Balanced Binary Tree

💡 Difficulty: Easy

🛠️ Topics: 遞迴與深度優先搜尋（DFS）、樹的高度計算、平衡樹的判斷、時間與空間複雜度

===============================================

Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Input: root = [1,2,3,null,null,4]
Output: true

Example 2:

Input: root = [1,2,3,null,null,4,null,5]
Output: false

Example 3:

Input: root = []
Output: true

Constraints:

．The number of nodes in the tree is in the range [0, 1000].

．-1000 <= Node.val <= 1000

=================================================

**UMPIRE Method:**

**Understand**

給定一棵二元樹，判斷這棵樹是否為高度平衡樹（height-balanced tree）。

．高度平衡樹的定義：每個節點的左、右子樹的高度差不超過 1。

步驟:
    1.輸入：給定二元樹的根節點 root。
    
    2.輸出：如果二元樹是高度平衡，返回 True；否則返回 False。
    
    3.特性：二元樹的每個節點左、右子樹的高度差不超過 1。

**Match**

這裡我們選擇使用 DFS（深度優先搜尋） 來遞迴檢查每個節點的平衡性，並計算子樹高度。這樣可以在單次遞迴中同時檢查平衡性和高度，避免重複遍歷，提升效率。

**Plan**

我們將使用遞迴函式 height(node) 來逐層檢查每個節點的左右子樹高度，並返回該節點的高度。如果遇到不平衡情況，即左右子樹的高度差大於 1，直接返回 -1 表示該節點不平衡。

計劃步驟：

    1.遞迴檢查左右子樹高度：自底向上計算每個節點的左右子樹高度。
    
    2.判斷平衡：若左右子樹高度差超過 1，則表示不平衡，回傳 -1。
    
    3.返回最終結果：若整棵樹均平衡，則返回根節點的高度；否則返回 False。

**Implement**

see solution.py

**Review**

此遞迴函式在遇到不平衡子樹時立即返回，避免不必要的計算。這樣的邏輯也符合高度平衡樹的條件，檢查是否精確且有效。

**Evaluate**

．時間複雜度：O(N)，其中 N 是樹的節點數。每個節點僅被訪問一次。

．空間複雜度：O(H)，其中 H 是樹的高度。遞迴調用堆疊的深度與樹的高度相同。




