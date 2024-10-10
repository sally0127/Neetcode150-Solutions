**Reverse a Linked List**
-
🔗 Link:Reverse a Linked List

💡 Difficulty: Easy

🛠️ Topics:

======================================================

Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:

Input: head = []
Output: []

Constraints:

．0 <= The length of the list <= 1000.

．-1000 <= Node.val <= 1000

====================================================

**UMPIRE Method:**

**Understand**

1.給定一個單鏈表的開頭 head，你需要將鏈表中的節點順序反轉。

2.返回新反轉的鏈表的開頭節點。

3.例如，給定鏈表：1 -> 2 -> 3 -> null，反轉後應該變成：3 -> 2 -> 1 -> null。

**Match**

我們可以使用以下幾個思路來解決：

．迭代法：逐步反轉鏈表中的節點指向，將當前節點的 next 指針改為指向前一個節點。

．递歸法：遞歸地將鏈表反轉，直到最後一個節點，並將節點逐步接回去。

**Plan**

我們使用迭代法，這是最常見且高效的解法。具體步驟如下：

1.初始化一個 prev 指針為空，用來追蹤已反轉部分的鏈表。

2.遍歷整個鏈表，逐步改變每個節點的 next 指針，使其指向前一個節點（即 prev）。

3.移動 prev 和 current 指針，直到遍歷完整個鏈表。

4.最終返回 prev，因為 prev 指向反轉後的頭節點。

**Implement**

see solution.py

**Review**

．代碼正確性：檢查代碼是否覆蓋了所有情況，特別是邊界情況（例如鏈表為空或者只有一個節點的情況）。

．邏輯檢查：確認是否正確地更新了指針，沒有造成死循環或指針丟失。

**Evaluate**

迭代法已經是最優的時間複雜度 O(n)和空間複雜度 O(1)，因為它只用了幾個額外的指針變量來完成鏈表反轉。

**思路**

1.也就是說，先儲存下一個node，這樣才能反轉節點的方向，轉換好方向後，把這兩個node交換過來，後面變成前面，前面變成後面，之後再換下一個node。

2.交換位置：把「前一個」移動到當前節點的位置，當前節點移到下一個節點，這算是更新prev，先更新prev才會有新的current。


