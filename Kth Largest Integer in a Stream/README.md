**Kth Largest Integer in a Stream**
-

🔗 Link: Kth Largest Integer in a Stream

💡 Difficulty: Easy

🛠️ Topics: 最小堆（Min-Heap）、動態數據流、插入和刪除操作

==================================================

Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

    ．constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
    
    ．int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

Example 1:

Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

Output:
[null, 3, 3, 3, 5, 6]

Explanation:

KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);

kthLargest.add(3);   // return 3

kthLargest.add(5);   // return 3

kthLargest.add(6);   // return 3

kthLargest.add(7);   // return 5

kthLargest.add(8);   // return 6

Constraints:

．1 <= k <= 1000

．0 <= nums.length <= 1000

．-1000 <= nums[i] <= 1000

．-1000 <= val <= 1000

．There will always be at least k integers in the stream when you search for the kth integer.

=================================================

**UMPIRE Method**

**Understand**

我們需要設計一個類別來處理動態數據流。這個類別的主要功能是：

    1.初始化：接受一個整數 k 和一個初始的整數流陣列 nums，並找到當前數據流中的第 k 大元素。
    
    2.添加元素：在數據流中添加一個整數 val，並返回此時數據流中的第 k 大元素。

範例： 假設 k=2，初始陣列 nums = [1, 2, 3, 3]，我們希望：

    ．初始化時，找到陣列中第 2 大的元素，這裡是 3。
    
    ．調用 add(4) 後，返回的第 2 大元素為 3。

注意：數據流不一定是排序的，且可能包含重複值。

**Match**

這是一個典型的 即時排序 問題，因為我們需要在每次添加新元素時，快速找到第 k 大的元素。

適用的資料結構和演算法：

    1.最小堆（Min-Heap）：我們可以利用一個大小為 k 的最小堆來追蹤數據流中的第 k 大元素。堆中保存第 k 大的元素和比它更大的元素。當添加新元素時，只需判斷是否需要將堆中的最小元素替換掉，從而保持堆的大小為 k。
    
    2.優先佇列：使用 Python 的 heapq 庫實現最小堆，可以有效地完成這個任務。

**Plan**

1.初始化：

    ．將陣列 nums 中的前 k 個元素插入到最小堆中。
    
    ．如果 nums 的元素多於 k 個，遍歷剩下的元素，對於每一個元素，若其大於最小堆的最小元素，則替換掉最小元素以保持第 k 大的值在堆頂。

2.添加新元素：

    ．將新元素 val 與最小堆的堆頂元素比較。
    
    ．若 val 大於堆頂元素，則用 val 替換堆頂，並重新調整堆。
    
    ．最小堆的堆頂即為第 k 大的元素。

**Implement**

see solution.py

**Review**

讓我們檢查代碼的正確性：

1.正確性：

    ．初始化時，透過 add 方法將 nums 中的元素逐一添加到最小堆中，這樣可以保證在初始化後，堆的大小始終為 k，且堆頂始終為第 k 大元素。
    
    ．add 方法根據數據流的變化動態調整最小堆，使得堆頂保持為第 k 大的元素。

**Evaluate**

時間複雜度：

    ．__init__ 方法的時間複雜度為 O(nlogk)，因為我們將 n 個元素逐一插入大小為 k 的堆中。
    
    ．add 方法的時間複雜度為 (logk)，因為插入操作或替換操作的時間複雜度取決於堆的大小 k。

空間複雜度：

    ．只存儲 k 個元素在最小堆中，因此空間複雜度為 O(k)。

**補充**

堆頂是指在堆（Heap）資料結構中的最上面一個元素。根據堆的類型（最小堆或最大堆），堆頂的含義有所不同：

1. **最小堆（Min-Heap）**：

   - 在最小堆中，堆頂是整個堆中最小的元素。這意味著每次從堆中刪除元素時，都是刪除最小的元素。

   - 例如，如果我們有一個最小堆 `[2, 3, 5, 7, 10]`，那麼堆頂就是 `2`。

2. **最大堆（Max-Heap）**：

   - 在最大堆中，堆頂是整個堆中最大的元素。這意味著每次從堆中刪除元素時，都是刪除最大的元素。

   - 例如，如果我們有一個最大堆 `[10, 7, 5, 3, 2]`，那麼堆頂就是 `10`。

### 堆的特性

- **層級結構**：堆通常以二元樹的形式實現，父節點的值總是小於（或大於）其子節點的值。
