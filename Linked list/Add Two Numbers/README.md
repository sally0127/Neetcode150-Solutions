**Add Two Numbers**
-
🔗 Link: Add Two Numbers

💡 Difficulty: Medium

🛠️ Topics: 鏈結串列遍歷(Linked List Traversal),進位處理(Carry Handling),建構新鏈結串列(Constructing a New Linked List)

====================================================

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:

Input: l1 = [1,2,3], l2 = [4,5,6]
Output: [5,7,9]

Explanation: 321 + 654 = 975.

Example 2:

Input: l1 = [9], l2 = [9]
Output: [8,1]

Constraints:

．1 <= l1.length, l2.length <= 100.

．0 <= Node.val <= 9

==================================================

**UMPIRE Method:**

**Understand**

1.問題：我們有兩個非空的鏈結串列 l1 和 l2，它們代表了兩個非負整數，數字以反向順序存儲。目標是將這兩個數字相加，並將結果作為新的鏈結串列返回。

2.輸入：兩個鏈結串列，每個節點代表一位數字。

3.輸出：一個新的鏈結串列，表示兩數之和。

**Match**

這題涉及基本的加法運算，尤其是在多位數的情境下處理進位。可以將此題比對到「小學數學中的加法運算」，從個位數開始逐位相加，同時處理進位。

**Plan**

1.初始化指針和變量：

．建立一個 dummy_head，用於結果鏈結串列的開頭。

．設置 current 指向 dummy_head，負責逐位生成結果鏈結串列。

．carry 初始為 0，用來記錄加法運算中的進位。

2.逐位相加：

．迴圈執行條件為 l1 或 l2 或 carry 為非零，確保處理所有位數。

．取得 l1 和 l2 當前節點的值（若節點為 None 則為 0）。

．計算當前位的和（sum = val1 + val2 + carry），並更新 carry = sum // 10。

．將 sum % 10 作為新節點的值，並加入到結果鏈結串列中。

3.移動指針：

．將 l1、l2 和 current 移動到下一個節點，準備處理下一位。

4.返回結果：

．返回 dummy_head.next 作為最終的結果鏈結串列頭部。

**Implement**

see solution.py

**Review**

1.確保所有情境都考慮到：包括不同長度的鏈結串列（如 l1 比 l2 長，或反之），以及最終進位的處理。

2.驗證結果：測試常見情況和邊界情況，例如：

．相同長度的鏈結串列。

．不同長度的鏈結串列。

．進位超過一位。

**Evaluate**

此實現的時間複雜度為 O(max(M,N))，其中 M 和 N 分別是 l1 和 l2 的長度。空間複雜度為 O(max(M,N))，用於儲存結果鏈結串列。

