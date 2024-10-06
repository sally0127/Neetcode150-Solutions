**Find Target in Rotated Sorted Array**
-
🔗 Link: Find Target in Rotated Sorted Array

💡 Difficulty: Medium

🛠️ Topics: 數據結構 (Data Structures),二分搜尋法 (Binary Search),邊界情況的處理 (Boundary Case Handling),條件邏輯 (Conditional Logic)

================================================================

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.

[1,2,3,4,5,6] if it was rotated 6 times.

Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2], target = 1
Output: 4

Example 2:

Input: nums = [3,5,6,0,1,2], target = 4
Output: -1

Constraints:

．1 <= nums.length <= 1000

．-1000 <= nums[i] <= 1000

．-1000 <= target <= 1000

=============================================================================

**UMPIRE Method**

**Understand**

1.數組 nums 是升序排列後被旋轉過的，且所有元素是唯一的。

2.我們需要找出 target 的索引位置；如果不存在，則返回 -1。

3.目標：用 O(log n) 的時間複雜度找出 target，這暗示需要用到二分搜尋法。

**Match**

使用 二分搜尋法。我們可以利用二分搜尋的優勢來縮小範圍，因為數組是有順序的，即使它被旋轉過，我們也能確定目標在某個範圍內。

**Plan**

1.設置兩個指標 left 和 right，分別指向數組的頭尾。

2.進行迭代，直到 left 超過 right。

3.在每次迭代中：

．計算中點 mid：mid = (left + right) // 2。

．如果 nums[mid] 恰好是 target，則返回 mid。

．否則，需要根據 nums[mid] 所在的範圍來確定如何移動 left 和 right 指標：

  ．判斷左半部分是否排序（即 nums[left] <= nums[mid]）：
  
    ．如果 target 在 nums[left] 和 nums[mid] 之間，則 target 在左半部分範圍內：right = mid - 1。
    
    ．否則，target 在右半部分範圍內：left = mid + 1。
    
  ．如果右半部分排序（即 nums[mid] <= nums[right]）：
  
    ．如果 target 在 nums[mid] 和 nums[right] 之間，則 target 在右半部分範圍內：left = mid + 1。
    
    ．否則，target 在左半部分範圍內：right = mid - 1。
    
4.如果迭代結束，未找到 target，返回 -1。

**Implement**

see solution.py

**Review**

．檢查每次 if-else 判斷的範圍是否能涵蓋所有可能性。

．確認我們的指標更新能夠適時縮小搜尋範圍，並避免陷入無限迴圈。

**Evaluate**

．時間複雜度：二分搜尋的時間複雜度為 O(logn)，滿足題目的需求。

．空間複雜度：O(1)，僅使用了有限的變量來儲存索引和計算結果。
