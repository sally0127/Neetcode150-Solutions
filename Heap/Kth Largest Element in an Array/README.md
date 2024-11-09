**Kth Largest Element in an Array**
-

🔗 Link: Kth Largest Element in an Array

💡 Difficulty: Medium

🛠️ Topics: 堆資料結構（Heap）、時間複雜度優化、遍歷與篩選

===========================================

Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:

Input: nums = [2,3,1,5,4], k = 2
Output: 4

Example 2:

Input: nums = [2,3,1,1,5,5,4], k = 3
Output: 4

Constraints:

．1 <= k <= nums.length <= 10000

．-1000 <= nums[i] <= 1000

=====================================================

**UMPIRE Method**

**Understand**

．輸入是一個未排序的整數陣列 nums 和一個整數 k。

．要找出陣列裡第 k 大的元素，這裡的 "第 k 大" 是指排序後第 k 大的值，而不是第 k 個不同的值。

．範例：

    ．輸入：nums = [3,2,1,5,6,4], k = 2
    
    ．輸出：5（排序後為 [6, 5, 4, 3, 2, 1]，第 2 大的元素是 5）

進階：

    ．要求一個不需要直接排序的解法，以提升效率。

**Match**

針對這個問題，可以考慮幾種解法：

1.排序法：直接將陣列排序，再取第 k 大的元素。時間複雜度是 O(nlogn)。

2.最小堆法：用一個大小為 k 的最小堆，時間複雜度是 O(nlogk)。遍歷陣列時，只保留前 k 大的元素，最後堆頂就是第 k 大的數。

3.快速選擇法：類似快速排序的分區算法，平均時間複雜度為 O(n)，最差情況是 O(n**2)。

在這裡，我們選擇 最小堆 的方法，因為它的時間複雜度較好，實現起來比快速選擇還簡單。

**Plan**

使用最小堆來解這題的步驟如下：

    1.先建立一個大小為 k 的最小堆，放入陣列的前 k 個元素。
    
    2.然後遍歷剩下的元素，對於每個元素：
    
      ．如果這個元素比堆頂（最小值）還大，就替換堆頂，並調整堆保持最小堆的性質。
      
      ．如果元素比堆頂小，就跳過不動。
      
    3.最後堆頂就是第 k 大的元素。

**Implement**

see solution.py

**Review**

1.邊界條件檢查：確認輸入是否為空、k 是否超出陣列長度。

2.正確性驗證：可以用幾組測試資料來驗證結果是否正確。

**Evaluate**

．時間複雜度：O(nlogk)。當 k 相對小時，這個方法比排序更高效。

．空間複雜度：O(k)，因為最小堆的大小固定為 k。

這種方法在較大的 n 和較小的 k 時非常高效，且程式碼清晰易懂。
