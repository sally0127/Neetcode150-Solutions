**Linked List Cycle Detection**
-
🔗 Link:Linked List Cycle Detection

💡 Difficulty: Medium

🛠️ Topics: 鏈結串列遍歷（Linked List Traversal）,快慢指針（Two-Pointer Technique）,空間效率（Space Efficiency）

============================================================

Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:

Input: head = [1,2,3,4], index = 1
Output: true

Example 2:

Input: head = [1,2], index = -1
Output: false

Constraints:

．1 <= Length of the list <= 1000.

．-1000 <= Node.val <= 1000

．index is -1 or a valid index in the linked list.

=============================================================

**UMPIRE Method:**

**Understand**

1.題目給出了一個鏈結串列的頭節點 head，需要判斷鏈結串列中是否存在 cycle。

2.如果至少有一個節點在遍歷過程中被再次拜訪到，即可判斷該鏈結串列中存在 cycle，應返回 true。

3.題目隱含信息：無法得知 index 具體位置，但當鏈結串列中有節點回指至之前的節點時，即形成 cycle；若尾節點的 next 指向 null，則表示沒有 cycle。

**Match**

在這題中可以對應到鏈結串列遍歷和快慢指針技巧：

．鏈結串列遍歷通常用來依次檢查每個節點。

．快慢指針技巧：設定兩個指針，以不同速度遍歷鏈結串列，可以有效檢查出是否存在 cycle。

**Plan**

1.3初始化快慢指針：

．設置兩個指針 slow 和 fast，皆指向 head。

．slow 每次向後移動一個節點，而 fast 每次向後移動兩個節點。

2.遍歷鏈結串列：

．當 fast 或 fast.next 為 null 時，表示沒有 cycle，返回 false。

．若 slow 與 fast 指向同一個節點，則表示存在 cycle，返回 true。

3.停止條件：

．當 fast 或 fast.next 為 null 時停止遍歷，這表示沒有 cycle。

**Implement**

see solution.py

**Review**

1.確保所有情況都已考慮：空鏈結串列（head 為 None）、無 cycle 的鏈結串列、存在 cycle 的鏈結串列。

2.測試結果：通過多種情況測試，例如鏈結串列中有 cycle 和無 cycle 的情況。

**Evaluate**

此實現的時間複雜度為 O(n)，因為 fast 指針每次移動兩個節點，故在最壞情況下只需遍歷一次鏈結串列。空間複雜度為 O(1)，僅使用了固定的指針變量。

