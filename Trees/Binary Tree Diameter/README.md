**Binary Tree Diameter**
-
🔗 Link: Binary Tree Diameter

💡 Difficulty: Easy

🛠️ Topics: 深度優先搜尋 (DFS)、遞迴 (Recursion)、後序遍歷 (Post-order Traversal)、最大路徑和最大深度

=============================================

The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:

Input: root = [1,null,2,3,4,5]
Output: 3

Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:

Input: root = [1,2,3]
Output: 2

Constraints:

．1 <= number of nodes in the tree <= 100

．-100 <= Node.val <= 100

=====================================================

**UMPIRE Method:**

**Understand**

1.找出二元樹的直徑（兩個節點之間的最長路徑）。

2.這條路徑不一定要經過根節點，可以經過任意兩個節點。

3.路徑的長度是邊的數量，而不是節點的數量。

**Match**

1.遞迴（Recursion）方法可以幫助我們從下往上計算每個節點的最長路徑。

2.使用 DFS（深度優先搜尋）和遞迴來獲取每個節點的左右子樹深度，計算從該節點通過的最大路徑。

**Plan**

1.定義一個輔助函數，計算每個節點的最大深度，同時更新全局變量 diameter 來儲存最長路徑。

2.對於每個節點，直徑可以表示為左子樹深度加右子樹深度。

3.遞迴地計算每個節點的最大深度，並在計算時更新直徑值。

4.返回計算出的 diameter。

**Implement**

see solution.py

**Review**

1.確認遞迴的基礎情況是否正確處理（即 node 為 None 時返回 0）。

2.確保每次遞迴更新 diameter 時，能捕捉當前的最大直徑。

3.計算每個節點的左右深度並正確加總。

**Evaluate**

．時間複雜度為 O(N)，其中 N是二元樹的節點數量，因為每個節點只被訪問一次。

．空間複雜度為 O(H)，其中 H 是樹的高度，遞迴的最大深度由樹的高度決定。
