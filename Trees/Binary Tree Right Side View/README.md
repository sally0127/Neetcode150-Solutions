**Binary Tree Right Side View**
-

🔗 Link: Binary Tree Right Side View

💡 Difficulty: Medium

🛠️ Topics: 層序遍歷 (Level Order Traversal)、右側視圖的定義、BFS（廣度優先搜索）策略

===================================================

You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:

Input: root = [1,2,3]
Output: [1,3]

Example 2:

Input: root = [1,2,3,4,5,6,7]
Output: [1,3,7]

Constraints:

．0 <= number of nodes in the tree <= 100

．-100 <= Node.val <= 100

==========================================================

**UMPIRE Method:**

**Understand**

1.給定一組二元樹，從右側觀看，回傳二元樹從上到下能看到的節點值。

2.目標是從根節點開始，只回傳每層最後一個節點的值，因為這些節點代表右側可見的節點。

**Match**

1.使用 BFS 可以逐層處理樹的節點，這樣每層都可以記錄最後一個節點的值。

2.BFS 遍歷時，從左到右處理每層的節點，這樣每層最後一個被處理的節點就是右側視角可見的節點。

**Plan**

以下是解題的步驟計畫：

1.初始化：若樹為空，直接返回空清單。

2.佇列設置：創建一個佇列並將根節點加入其中。

3.層級遍歷：

    ．依序從佇列中取出當前層的節點，並從左到右處理每層的所有節點。
    
    ．每層最後一個節點的值就是右側可見的節點，將其值加入結果清單中。

4.加入子節點：對於每個節點，依序將其左子節點和右子節點加入佇列。

5.當 BFS 結束時，返回結果清單。

**Implement**

see solution.py

**Review**

1.確認邊界情況：當 root 為 None 時，返回空清單 []。

2.正確性檢查：檢查是否只返回每層的最後一個節點，並且按順序存儲在結果清單中。

3.效率：BFS 可以逐層遍歷，適合從樹的右側視角進行層級遍歷。

**Evaluate**

1.時間複雜度：由於 BFS 遍歷所有節點，時間複雜度是 O(n)，其中 n 是節點數。

2.空間複雜度：佇列和結果清單都會儲存每層節點，因此空間複雜度為 O(n)。

