**Reverse Nodes in K-Group**
-

🔗 Link: Reverse Nodes in K-Group

💡 Difficulty: Hard

🛠️ Topics: 鏈表操作 (Linked List Manipulation)、分組反轉 (Group Reversal)、輔助函數的使用 (Helper Function for Reversal)、邊界情況的處理 (Handling Edge Cases)、時間和空間複雜度分析 (Time and Space Complexity Analysis)

===========================================

You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:

Input: head = [1,2,3,4,5,6], k = 3
Output: [3,2,1,6,5,4]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:

．The length of the linked list is n.

．1 <= k <= n <= 100

．0 <= Node.val <= 100

=================================================

**UMPIRE Method:**

**Understand**

1.問題概述：

    ．給定一個單向鏈表，將它按每 k 個節點為一組進行反轉。如果剩餘的節點少於 k，則保持這些節點的順序不變。
    
    ．關鍵點是：不可以更改節點的值，只能調整節點的 next 指針。

2.範例：

    ．如果輸入是鏈表 1 -> 2 -> 3 -> 4 -> 5，k=2，則返回 2 -> 1 -> 4 -> 3 -> 5。
    
    ．若 k=3，則鏈表變為 3 -> 2 -> 1 -> 4 -> 5。

3.約束條件：

    ．鏈表長度未知，鏈表節點可能少於 k 個，特別要考慮尾部少於 k 的情況。

**Match**

這是一個“鏈表的分段反轉”問題，可以按照以下步驟解決：

1.遍歷與計數：先遍歷鏈表，確定分段數。

2.分段反轉：對每段 k 個節點的部分執行反轉，每次反轉完成後重新連接已反轉的部分和未反轉的部分。

3.特殊情況處理：如果剩餘節點少於 k，則保持原樣，不做反轉。

**Plan**

1.計數節點：遍歷鏈表，計算總節點數。

2.反轉每段：用一個循環，每次反轉 k 個節點，直到剩餘的節點數小於 k。

3.反轉子函數：實現一個輔助函數 reverseKNodes，用於反轉鏈表中某個區段的 k 個節點。

4.連接部分：每次反轉後，將上一次反轉的尾節點與下一段反轉的頭節點連接起來。

5.返回新頭節點：完成所有反轉操作後，返回新的鏈表頭節點。

．反轉每段是在主程式中進行的迴圈操作，負責分段控制與管理，決定是否需要對當前區段進行反轉。

．反轉子函數則負責實際反轉每一個 k 節點區段的指標，是具體的反轉實作。

簡單來說，反轉每段的主程式邏輯就像是在分配任務：它負責找出哪些區段需要反轉，然後把這些區段交給反轉子函數來實際執行反轉操作。這樣的結構讓我們可以重複利用反轉子函數，每次只針對單一區段執行反轉，而不用重新寫反轉邏輯。

這種分工在鏈表和其他複雜數據結構題目中非常常見，可以讓代碼更具模組化，也讓你更清楚地知道每部分的責任。

**Implement**

see solution.py

**Review**

1.正確性檢查：檢查邊界條件，比如空鏈表、鏈表長度小於 k、最後一段長度小於 k 等情況。

2.程式碼閱讀性：代碼清晰易讀，輔助函數 reverseKNodes 將反轉邏輯分離出來，使得主邏輯更簡潔。

**Evaluate**

1.時間複雜度：我們需要遍歷鏈表的每個節點一次，因此時間複雜度為 O(n)。

2.空間複雜度：僅使用了常數輔助變量，因此空間複雜度為 O(1)。

3.性能和效能：該實現能在合理時間內完成大量節點的反轉，並對每個邊界情況進行了妥善處理。

