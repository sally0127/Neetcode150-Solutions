**Valid Binary Search Tree**
-

🔗 Link: Valid Binary Search Tree

💡 Difficulty: Medium

🛠️ Topics: 遞迴(DFS)、二元搜尋樹 (BST) 的特性

====================================================

Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

    ．The left subtree of every node contains only nodes with keys less than the node's key.
    
    ．The right subtree of every node contains only nodes with keys greater than the node's key.
    
    ．Both the left and right subtrees are also binary search trees.

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [1,2,3]
Output: false

Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

Constraints:

．1 <= The number of nodes in the tree <= 1000.

．-1000 <= Node.val <= 1000

=================================================

**UMPIRE Method**

**Understand**

1.問題目標：給定一棵二元樹，判斷這棵樹是否為有效的二元搜尋樹。

2.有效的 BST 條件：

    ．對於每個節點，其左子樹的所有節點值均小於該節點值，右子樹的所有節點值均大於該節點值。
    
    ．左子樹和右子樹也必須符合二元搜尋樹的條件。

3.輸出：若為有效的 BST，回傳 true；否則回傳 false。

**Match**

1.使用 DFS 深入搜尋可以有效地檢查每一個子樹是否符合 BST 條件。

2.在遞迴過程中，可以使用上下界來約束每個節點的值，從而保證 BST 的有效性。

    ．當遞迴到左子樹時，設置右邊界為當前節點的值。
    
    ．當遞迴到右子樹時，設置左邊界為當前節點的值。

**Plan**

1.建立一個遞迴函數，該函數接收當前節點和允許的值範圍（min_val 和 max_val）。

2.如果節點為空，則直接回傳 true，表示到達葉節點。

3.如果節點的值不在 min_val 和 max_val 範圍內，則回傳 false。

4.遞迴檢查左子樹和右子樹：

    ．對左子樹，設置當前節點值為右邊界（max_val）。
    
    ．對右子樹，設置當前節點值為左邊界（min_val）。

5.如果左右子樹均符合條件，則返回 true；否則返回 false。

**Implement**

see solution.py

**Review**

1.正確性檢查：

    ．左、右子樹的遞迴範圍條件設置正確，確保每個節點都被限制在正確的值範圍內。
    
    ．min_val 和 max_val 準確地在每個遞迴層次中更新。

2.邊界條件：

    ．空樹（root == None）應該返回 true，因為空樹視為有效 BST。
    
    ．具有單一節點的樹，應返回 true。
    
    ．檢查包含重複值的情況，例如 [2, 1, 2] 應返回 false。

**Evaluate**

．時間複雜度為 O(n)，其中 n 是節點數，每個節點被訪問一次。

．空間複雜度為 O(h)，其中 h 是樹的高度，用於遞迴堆疊。

**補充**

這題的主要概念是**遞迴**和**二元樹的性質**。在檢查是否是有效的二元搜尋樹 (BST) 時，需要了解以下幾個關鍵概念：

1. **二元搜尋樹 (BST) 的特性**：

   - 每個節點的左子樹的所有節點值必須小於該節點值。

   - 每個節點的右子樹的所有節點值必須大於該節點值。

   - 這些條件必須遞迴地適用於每個節點。

2. **遞迴範圍限制**：

   - 在檢查每個節點時，會遞迴地向下檢查左、右子樹，同時為左右子樹設置一個有效的值範圍。

   - 左子樹的節點值範圍是 `(min_val, node.val)`，而右子樹的節點值範圍是 `(node.val, max_val)`，這樣確保左子樹和右子樹的每個節點都符合 BST 規則。

4. **遞迴停止條件**：

   - 當遞迴到空節點時，返回 `True`，表示空節點符合 BST 規則。

   - 若發現節點值不在範圍 `(min_val, max_val)` 內，則該節點不符合 BST 規則，返回 `False`。

這些概念結合起來構成了**深度優先搜索 (DFS)** 的檢查方式。DFS 方式有效地遍歷樹中的每個節點，同時確保每個節點都符合 BST 的定義，這樣可以逐層確認整個樹是否是一個有效的二元搜尋樹。



