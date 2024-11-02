**Binary Tree Maximum Path Sum**
-
🔗 Link: Binary Tree Maximum Path Sum

💡 Difficulty: Hard

🛠️ Topics: 遞迴與分治法、動態規劃思想、後序遍歷、剪枝與優化、全局變數紀錄最大值

===================================================

Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can not appear in the sequence more than once. The path does not necessarily need to include the root.

The path sum of a path is the sum of the node's values in the path.

Example 1:

Input: root = [1,2,3]
Output: 6

Explanation: The path is 2 -> 1 -> 3 with a sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-15,10,20,null,null,15,5,-5]
Output: 40

Explanation: The path is 15 -> 20 -> 5 with a sum of 15 + 20 + 5 = 40.

Constraints:

．1 <= The number of nodes in the tree <= 1000.

．-1000 <= Node.val <= 1000

=======================================================

**UMPIRE Method:**

**Understand**

1.題目描述：

    ．給定一個非空的二元樹，求出任意一條非空路徑的最大路徑和。
    
    ．路徑可以從任何節點開始並在任何節點結束，不需要包含根節點，但每個節點只能訪問一次。
    
    ．路徑和是這條路徑中所有節點值的和。

2.重要條件：

    ．樹的節點可以包含負數。
    
    ．目標是找到一條具有最大路徑和的路徑。

**Match**

1.方法選擇：這題適合用遞迴（DFS 深度優先搜索）解決。

2.觀察：

    ．在每個節點，我們可以計算以這個節點為起點的路徑和。
    
    ．遍歷到某節點時，需要記錄它的左右子樹的最大路徑和，然後決定是否要包括該節點進行最大和的更新。

**Plan**

1.使用 DFS 遞迴計算每個節點的最大貢獻值：

    ．計算左子樹和右子樹的最大路徑和，並對每個節點進行更新。

2.決定是否更新全局最大和 max_sum：

    ．若當前節點的路徑和（包括左右子樹和自己）比目前已知的最大和大，則更新 max_sum。

3.返回節點的貢獻值：

    ．對於父節點的遞迴，返回此節點和其左右子樹中的最大路徑和（只選一側）之和，這樣可以保持路徑連續性。

**Implement**

see solution.py

**Review**

1.檢查邊界條件：

    ．單個節點的情況。
    
    ．所有節點都是負數的情況。

2.確認 DFS 的返回值是否只返回給上層節點最大的單側路徑，確保路徑不斷裂。

**Evaluate**

．時間複雜度：每個節點只會被訪問一次，時間複雜度為 O(N)，其中 N 是節點總數。

．空間複雜度：因為使用了遞迴，空間複雜度為 O(H)，其中 H 是樹的高度。


