**Level Order Traversal of Binary Tree**
-

🔗 Link: Level Order Traversal of Binary Tree

💡 Difficulty: Medium

🛠️ Topics: 廣度優先搜尋 (BFS)、佇列的使用、分層處理、不平衡樹的處理

=================================================

Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

．0 <= The number of nodes in both trees <= 1000.

．-1000 <= Node.val <= 1000

=============================================================

**UMPIRE Method:**

**Understand**

問題說明：

．給定一棵二元樹，要求進行 層序遍歷（Level Order Traversal）。

．要回傳一個 巢狀清單（nested list），裡面每個子清單都代表樹的一個層級，從左到右按順序擺放該層所有節點的值。

舉例說明： 假設這棵樹結構是這樣：

        3
       / \
      9  20
         / \
        15  7

那麼，層序遍歷結果應該是 [[3], [9, 20], [15, 7]]。

**Match**

這題的層序遍歷其實是 樹的廣度優先搜尋（BFS） 的經典應用，所以 利用 BFS 遍歷會更適合。使用 BFS 的好處是：

1.BFS 是天然的逐層遍歷，每一層節點會依序被探索。

2.可以使用 佇列（Queue） 來實現，每次把當前層的節點逐一出佇列並擴展到下一層。

因此，使用 BFS 和佇列來解會比遞迴法更有效。

**Plan**

1.初始化資料結構：建立一個空的清單 result 來儲存每一層的節點值，並用佇列 queue 來進行 BFS。

2.放入根節點：先將根節點 root 加入 queue 中，如果 root 是空的，就直接回傳空的 result。

3.逐層處理：

    ．當 queue 裡還有節點時，我們就一層一層處理。
    
    ．在每一層，記錄當前 level_size，這個值就是當前層的節點數量。
    
    ．使用一個 level 清單來儲存當前層的節點值。

4.擴展下一層：對於每一層的每個節點：

    ．取出節點，將它的值加入 level。
    
    ．若該節點有左或右子節點，把它們加入 queue，這樣下一層就會被處理。

5.存入結果：當當前層的所有節點都處理完，就把 level 加入 result。

6.回傳：當所有層都遍歷完後，回傳 result。

**Implement**

see solution.py

**Review**

1.佇列的初始化：包含根節點的情況正確處理了。

2.逐層處理：每層的節點值正確加入 level，每層完結後也成功加入 result。

3.邊界情況：確認根節點為空的情況處理無誤，回傳空的 result。

**Evaluate**

．時間複雜度：O(n)，因為每個節點只會被處理一次。

．空間複雜度：O(n)，最壞情況下，最後一層節點數會達到 n/2，所以在佇列中會存儲大約 n/2 的節點。



