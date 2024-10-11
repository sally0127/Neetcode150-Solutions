**Merge Two Sorted Linked Lists**
-
🔗 Link:*Merge Two Sorted Linked Lists

💡 Difficulty: Easy

🛠️ Topics: 鏈結串列的操作(Linked List Manipulation),排序維護(Maintaining Order),基礎指標操作(ex:虛擬節點（dummy node）)

========================================================

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:

Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:

Input: list1 = [], list2 = []
Output: []

Constraints:

．0 <= The length of the each list <= 100.

．-100 <= Node.val <= 100

===========================================================

**UMPIRE Method:**

**Understand**

問題要求：

．給定兩個排序好的鏈結串列 list1 和 list2 的頭節點。

．合併這兩個鏈結串列成為一個排序好的鏈結串列，並返回新的頭節點。

目標：

．將 list1 和 list2 的節點合併到一個新鏈結串列中，並保持順序。

．新的鏈結串列必須包含來自 list1 和 list2 的所有節點，不會創建新的節點，而是重用現有的節點。

**Match**

們可以使用以下方法來解決問題：

1.迭代法：

．建立一個虛擬頭節點（dummy node）和一個指標 current 用於構建新鏈結串列。

．比較 list1 和 list2 當前節點的值，選擇較小的節點並將 current 指向它，並移動指針。

．重複以上步驟直到遍歷完整個鏈結串列。

．最後，將剩餘的鏈結串列（list1 或 list2）連接到 current 的尾部。

2.遞迴法：

．比較 list1 和 list2 當前節點的值，選擇較小的節點，並遞迴處理餘下的節點。

．使用遞迴函式逐步合併並構建新鏈結串列。

**Plan**

使用迭代法的詳細步驟：

1.建立一個虛擬頭節點 dummy 以及一個指標 current。

2.當 list1 和 list2 都不為空時，進行以下操作：

．比較 list1 和 list2 當前節點的值。

．將 current.next 指向較小的節點，並移動該節點和 current 的位置。

3.當一個鏈結串列為空時，將另一個鏈結串列剩下的部分接到 current.next。

4.返回 dummy.next 作為新鏈結串列的頭節點。

**Implement**

see solution.py

**Review**

1.檢查特殊情況：例如 list1 或 list2 為空的情況，這樣可以確保代碼覆蓋所有邊界情況。

2.確保合併後的鏈結串列順序正確。

3.檢查是否每個節點都正確地包含在新鏈結串列中，避免節點丟失或循環錯誤。

**Evaluate**

1.時間複雜度：

．由於我們需要遍歷 list1 和 list2 的每個節點，因此時間複雜度為 O(n + m)，其中 n 和 m 是 list1 和 list2 的節點數量。

2.空間複雜度：

．使用的額外空間是常數 O(1)，因為我們只用了幾個指標變數來完成合併。

**主要想法**

這是我的理解，步驟1:先創建一個虛擬結頭和箭頭，箭頭指向虛擬結頭 步驟2:當list1和list2不為空時，比較list1和list2的值，看哪一個比較小，就將current.val指向較小的值，並移動箭頭和節點。

current.next = list1 if list1 else list2 這一行的作用，處理當其中一個鏈結串列（list1 或 list2）已經遍歷完的情況。因為 list1 和 list2 一開始就是排序好的，所以當其中一個鏈結串列跑完時，另一個鏈結串列剩下的部分其實已經是整體排序中的最大部分，因此可以直接接到 current.next 上。

具體情況分析:

1.假如 list1 先跑完（list1 變成 None），這行代碼會讓 current.next = list2，把 list2 剩餘的部分直接接到 current 後面。

2.如果是 list2 先跑完（list2 變成 None），這行代碼會讓 current.next = list1，把 list1 剩餘的部分接到 current 後面。

例子分析:

假設 list1 是 1 -> 3 -> 5，list2 是 2 -> 4 -> 6 -> 7，迭代合併後的部分會變成：

．1 -> 2 -> 3 -> 4 -> 5 -> 6（到此為止，list1 遍歷完了）

．此時，list2 還有 7 沒有接上，這行代碼會自動把 7 接到 current.next，最終結果是 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
