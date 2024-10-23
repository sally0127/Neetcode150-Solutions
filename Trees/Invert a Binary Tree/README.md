**Invert a Binary Tree**
-
🔗 Link:Invert a Binary Tree

💡 Difficulty: Easy

🛠️ Topics:二元樹（Binary Tree）,遞迴（Recursion）,左右子樹對調（Subtree Swapping）,遍歷樹（Tree Traversal）

==================================================

You are given the root of a binary tree root. Invert the binary tree and return its root.

Example 1:

Input: root = [1,2,3,4,5,6,7]

Output: [1,3,2,7,6,5,4]

Example 2:

Input: root = [3,2,1]

Output: [3,1,2]

Example 3:

Input: root = []

Output: []

Constraints:

．0 <= The number of nodes in the tree <= 100.

．-100 <= Node.val <= 100

=======================================================

**UMPIRE Method:**

**Understand**

．你已經了解了這部分：給你一棵二元樹，你需要把它反轉，也就是每個節點的左邊和右邊的子樹對調。

．明確需求：最終要傳回反轉後的樹根。

**Match**

．資料結構類型：這是一個經典的二叉樹問題。

．算法類型：用遞迴（遞歸）或者是迭代方法來處理都可以。

通常來說，反轉二元樹可以用 遞迴 或者 深度優先搜索（DFS）、廣度優先搜索（BFS） 來解。用遞迴會比較直觀，因為直接把每個節點的左右子樹做處理就好。

**Plan**

這邊我們用 遞迴 來反轉二元樹，以下是具體步驟：

1.基礎情況（Base Case）：如果當前節點是空的（root == null），就直接回傳 null。

2.遞迴步驟：
    
    ．先遞迴處理左邊的子樹。
    
    ．再遞迴處理右邊的子樹。
    
    ．最後對調左右子樹。

3.傳回根節點：處理完後，傳回反轉後的樹根。

步驟簡單說：


    1.先遞迴處理左右子樹。
    
    2.把左右子樹對調。
    
    3.最後回傳根節點。

**Implement**

see solution.py

**Review**

．邊界情況：
    
    ．空樹：root 為空時，應該直接回傳 None。
    
    ．單個節點的樹：沒有左右子樹的情況會正確處理。
    
    ．對於一般的樹結構，遞迴處理左右子樹並交換，確保反轉效果正確。

**Evaluate**

．時間複雜度：每個節點會被訪問一次，所以時間複雜度是 O(n)，n 是樹裡面的節點數。

．空間複雜度：遞迴的堆疊深度是 O(h)，h 是樹的高度，最壞的情況（像是樹變成鏈狀）下空間複雜度會是 O(n)。
