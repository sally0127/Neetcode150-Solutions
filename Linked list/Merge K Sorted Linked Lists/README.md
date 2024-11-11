**Merge K Sorted Linked Lists**
-

🔗 Link: Merge K Sorted Linked Lists

💡 Difficulty: Hard

🛠️ Topics: 優先級隊列（Min-Heap）的應用、分治策略（Divide and Conquer）、優化合併多個排序鏈表的問題

============================================

You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:

Input: lists = [[1,2,4],[1,3,5],[3,6]]
Output: [1,1,2,3,3,4,5,6]

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

．0 <= lists.length <= 1000

．0 <= lists[i].length <= 100

．-1000 <= lists[i][j] <= 1000

===============================================

**UMPIRE Method**

**Understand**

我們有一組已經排好序的鏈表，目標是將這些鏈表合併成一個新的已經排序好的鏈表。這是一個經典的合併多個已排序鏈表的問題。

**Match**

在這裡，我們選擇使用 最小堆 (min-heap)，因為最小堆允許我們每次高效地提取最小的元素，並能夠快速地將元素插入堆中，從而合併多個鏈表。

    最小堆的優點：
    
    ．每次從堆中提取最小的元素，這樣就能夠保證合併的鏈表順序正確。
    
    ．時間複雜度：插入和刪除堆元素的時間複雜度是 O(logk)，其中 k 是鏈表的數量。對每個節點進行處理需要 O(nlogk)，其中 n 是所有鏈表中節點的總數。

**Plan**

1.初始化堆並加入頭節點：每個鏈表的頭節點先加入 heap。這時，heap 內部會根據 __lt__ 方法排序。

2.從 heap 中取出最小的節點：每次 heappop 操作都會取出當前 heap 中最小的節點（根據 val 值）。

3.加入結果鏈表：將這個最小節點接到結果鏈表的尾部。

4.加入後繼節點：如果該節點有下一個節點，將其加入 heap。heap 隨後會自動排序，以保持堆的有序性。

5.重複步驟 2 到 4：不斷取出最小節點並加入結果鏈表，直到 heap 變空。

這樣，heap 在每次取出和加入節點時都會進行排序，確保總是按順序合併鏈表。

**Implement**

see solution.py

**Review**

這段代碼應該能夠順利運行，將三個已經排序的鏈表合併為一個新的鏈表。假設輸入的鏈表為：

．1 -> 4 -> 5

．1 -> 3 -> 4

．2 -> 6

合併後的結果應該是：

    1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None

**Evaluate**

．時間複雜度: O(nlogk)，其中 n 是總節點數，k 是鏈表的數量。

．空間複雜度: O(k+n)，其中 k 是鏈表的數量，n 是總節點數。





