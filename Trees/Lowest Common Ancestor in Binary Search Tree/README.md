**Lowest Common Ancestor in Binary Search Tree**
-
🔗 Link: Lowest Common Ancestor in Binary Search Tree

💡 Difficulty: Medium

🛠️ Topics: 二元搜尋樹（Binary Search Tree, BST）特性、遞迴與迭代的選擇、最低公共祖先（Lowest Common Ancestor, LCA）、分治法的概念、時間與空間複雜度分析

==========================================

Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

Example 1:

Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
Output: 5

Example 2:

Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
Output: 3

Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

Constraints:

．2 <= The number of nodes in the tree <= 100.

．-100 <= Node.val <= 100

．p != q

．p and q will both exist in the BST.

===========================================================

**UMPIRE Method:**

**Understand**

問題說明： 我們有一棵 二元搜尋樹（Binary Search Tree, BST），要找兩個節點 p 跟 q 的 最低共同祖先（Lowest Common Ancestor, LCA）。所謂的「最低共同祖先」就是說，在這棵樹裡找到最低的那個節點，這個節點能當 p 跟 q 的祖先。

舉例來說：

假設 BST 是這樣的結構：

      6
     / \
    2   8
   / \ / \
  0  4 7  9
    / \
   3   5

．假設 p = 2，q = 8，那麼 LCA 就是 6。

．如果 p = 2，q = 4，LCA 就是 2。

重點：

．這是一棵二元搜尋樹，也就是說，左子樹的值都比較小，右子樹的值都比較大，而且每個節點的值都是獨一無二。

**Match**

因為這是 BST，所以咱們可以利用 BST 的特性，快速找到 LCA。簡單來說，對於 BST 裡的任意節點 root：

．若 p 跟 q 的值都比 root 小，LCA 一定在 root 的左子樹。

．若 p 跟 q 的值都比 root 大，LCA 一定在 root 的右子樹。

．若 p 跟 q 分別位在 root 的兩邊（或其中一個剛好等於 root），那 root 就是 LCA。

**Plan**

解題思路：

1.從根節點開始遍歷 BST。

2.檢查現在的節點 root.val：

    ．若 p.val < root.val 且 q.val < root.val，代表 LCA 在左邊，咱們就往 root.left 繼續找。
    
    ．若 p.val > root.val 且 q.val > root.val，代表 LCA 在右邊，咱們就往 root.right 繼續找。
    
    ．若 p 和 q 分別在左右子樹，或其中一個等於 root，就表示 root 是 LCA，直接回傳 root。

**Implement**

see solution.py

**Review**

．確保咱們的邏輯沒問題，特別是檢查 p 和 q 的值相對於 current 的值，確認我們往正確方向移動。如果 p 和 q 分別在 current 的兩側，那這個 current 就是 LCA。

．時間效率：平均情況下這是 O(log n)，相當快。

．正確性：利用 BST 的特性，咱們每一步都確保走在對的路徑上。邊界條件例如 p 跟 q 分別在根的左右子樹或其中一個是另一個的祖先，這些情況都已經覆蓋到了。

**Evaluate**

．時間複雜度：平均來說是 O(log n)，因為我們只要沿著樹的一條路徑往下走就好。

．空間複雜度：O(1)，因為咱們沒有用到額外的空間。

