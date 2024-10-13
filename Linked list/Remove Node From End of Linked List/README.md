**Remove Node From End of Linked List**
-
🔗 Link: Remove Node From End of Linked List

💡 Difficulty: Medium

🛠️ Topics: 鏈結串列操作 (Linked List Operations),雙指針技術 (Two-Pointer Technique),時間與空間複雜度 (Time and Space Complexity),邊界情況處理 (Edge Case Handling)

=====================================================

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:

Input: head = [5], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 2
Output: [2]

Constraints:

．The number of nodes in the list is sz.

．1 <= sz <= 30

．0 <= Node.val <= 100

．1 <= n <= sz

=============================================================

**UMPIRE Method:**

**Understand**

1.給定一個單向鏈結串列的開頭 head 和一個整數 n。

2.需要移除鏈結串列倒數第 n 個節點，並返回新的鏈結串列的開頭 head。

**Match**

1.利用雙指針法解決問題，這是一種有效且常見的鏈結串列操作方法。

2.使用雙指針讓其中一個指針先行 n 步，然後再與另一個指針同時前進，直到前面的指針到達鏈結串列的尾部。這樣後面的指針就會正好停在倒數第 n 個節點的前一個節點位置。

**Plan**

1.初始化指針：設定兩個指針 fast 和 slow，都指向 head 開始的位置。

2.移動 fast 指針：將 fast 向前移動 n 步，確保 fast 與 slow 指針之間相隔 n 個節點。

3.同步移動 fast 和 slow：當 fast 指針到達鏈結串列末尾時，slow 指針正好指向倒數第 n 個節點的前一個節點。

4.刪除節點：將 slow.next 指向 slow.next.next，從而跳過倒數第 n 個節點，達到刪除的效果。

5.特殊情況處理：如果 n 等於鏈結串列的長度（也就是 fast 起點就在要刪除的節點），我們可以直接返回 head.next，因為這種情況下刪除的就是頭節點。

6.返回新鏈結串列的頭部。

**Implement**

see solution.py

**Review**

1.邏輯檢查：檢查刪除操作是否會處理到鏈結串列的末尾或頭部節點。

2.邊界條件：確保鏈結串列中節點數少於 n 時不會引發錯誤，例如當 n 等於鏈結串列的長度時是否能正確處理。

**Evaluate**

複雜度分析：時間複雜度為 O(L)，其中 L 是鏈結串列的長度。空間複雜度為 O(1)。

