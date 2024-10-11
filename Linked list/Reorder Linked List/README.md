**Reorder Linked List**
-
🔗 Link: Reorder Linked List

💡 Difficulty:Medium

🛠️ Topics: 

====================================================

You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:

Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]

Constraints:

．1 <= Length of the list <= 1000.

．1 <= Node.val <= 1000

==================================================================

**UMPIRE Method:**

**Understand**

1.輸入：給定一個單鏈結串列（由頭節點 head 表示）。

2.輸出：將鏈結串列重排序，使節點位置從 [0, n-1, 1, n-2, 2, n-3, …]。

3.限制：不能改變節點的值，只能改變節點指向順序。

範例：

輸入：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7

輸出：1 -> 7 -> 2 -> 6 -> 3 -> 5 -> 4

**Match**

解決這個問題有以下幾種方法，這裡我們選擇 分步迭代法：

1.使用「快慢指針」找出鏈結串列的中點。

2.將中點後的鏈結串列反轉。

3.將兩個鏈結串列按所需順序合併。

**Plan**

1.找到中點：使用快慢指針來定位中點。快指針每次移動兩步，慢指針移動一步，當快指針到達尾端時，慢指針就位於中點。

2.反轉後半段鏈結串列：從中點後開始反轉鏈結串列的後半部分。這樣就可以得到兩個鏈結串列，前半部分保持順序，後半部分倒序。

3.合併兩部分：將兩部分的節點依照 0, n-1, 1, n-2 交替合併，形成所需的排列順序。

**Implement**

see solution.py

**Review**

1.正確性：確認代碼是否能正確找到中點，反轉後半部分，並交替合併。

2.邊界情況：測試包含 0 個、1 個或 2 個節點的鏈結串列。

**Evaluate**

此解法的時間複雜度是 O(n) 因為每個節點只被遍歷一次。空間複雜度是 O(1)，因為沒有使用額外的儲存空間。

**理解思路**

步驟1:找出中點，先設定slow、fast在起點，然後當fast和fast.next都不為None時才繼續執行迴圈。slow設定往前一個節點，fast設定會向前兩個節點。 

步驟2:設定prev和curr，因為要反轉後半段，所以將slow.next的結尾指向None， 先設定next_node會變成curr.next，之後轉變箭頭方向，這樣curr.next 會變成 prev，prev才會變成curr，curr才會變成下一個節點，這樣就代表已成功反轉後半段。

步驟3: 先設定first和second的下一個節點，分別是temp1和temp2。 然後first.next = second，將前半部分的當前節點 first 的 next 指向後半部分的當前節點 second，這樣，合併後的鏈結串列就會出現 first -> second 的順序。

second.next = temp1，將 second 的 next 指向 first 的下一個節點 temp1，這樣 second 和下一個 first 就會被正確地連接起來，這一步確保合併後的鏈結串列順序正確，例如 first -> second -> first.next。

first, second = temp1, temp2，移動 first 和 second 指針到下一個節點（即 temp1 和 temp2），準備進行下一輪交錯合併，每次迴圈都會更新 first 和 second，直到後半部分的 second 為 None，迴圈結束，合併完成。
      
   



