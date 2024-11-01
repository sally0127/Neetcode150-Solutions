**Count Good Nodes in Binary Tree**
-

🔗 Link: Count Good Nodes in Binary Tree

💡 Difficulty: Medium

🛠️ Topics: 深度優先搜索 (DFS)、路徑中的最大值追踪、二元樹的遞迴處理、條件判斷與計數

=============================================

Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:

Input: root = [2,1,1,3,null,1,5]
Output: 3

Example 2:

Input: root = [1,2,-1,3,4]
Output: 4

Constraints:

．1 <= number of nodes in the tree <= 100

．-100 <= Node.val <= 100

====================================================

**UMPIRE Method**

**Understand**

1.我們需要找出從根節點到某節點的路徑中，該節點的值是否為最大的，若是，則稱其為「好節點」。

2.給定二元樹的根節點 root，返回其中「好節點」的總數。

**Match**

1.使用 DFS (深度優先搜索) 更適合這題：DFS 讓我們可以追踪從根節點到當前節點的路徑，並且持續更新在該路徑中遇到的最大值。每當我們遇到一個節點的值大於或等於路徑中的最大值，這個節點即為「好節點」。

2.DFS 遞迴：透過遞迴或使用堆疊進行 DFS，我們可以在每次遞迴中傳遞當前路徑的最大值。

**Plan**

1.定義遞迴函數 dfs(node, max_val)：

    ．如果 node 為空，直接返回 0。
    
    ．若 node.val >= max_val，則它是一個「好節點」，計數加 1。
    
    ．更新 max_val 為 max(node.val, max_val)，以便對該節點之後的子節點進行比較。
    
    ．對左右子節點進行遞迴調用，並將「好節點」的總數返回。

2.在主函數中，從根節點開始，初始化 max_val 為根節點的值並調用遞迴函數。

**Implement**

see solution.py

**Review**

1.檢查遞迴終止條件：if not node: return 0，確保空節點直接返回而不影響結果。

2.確認最大值更新：每次遞迴都更新 max_val 為當前路徑的最大值，以便後續子節點正確比較。

3.邊界情況：確認當樹為空時正確返回 0。

**Evaluate**

．時間複雜度：每個節點只遍歷一次，因此時間複雜度為 O(N)，其中 N 是節點數。

．空間複雜度：遞迴深度的空間複雜度為 O(H)，其中 H 是樹的高度。在最壞情況（例如單鏈表形式的樹）下，遞迴深度可能達到 O(N)。

這樣的方法可以有效地解決「好節點」計數問題，並充分利用 DFS 追踪路徑上的最大值。

