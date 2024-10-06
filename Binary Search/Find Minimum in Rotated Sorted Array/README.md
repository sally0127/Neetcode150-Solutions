**Find Minimum in Rotated Sorted Array**
-
🔗 Link: Find Minimum in Rotated Sorted Array

💡 Difficulty: Medium

🛠️ Topics: Data Structures,Binary Search,Boundary Case Handling,Mathematical Properties 

==========================================================

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

．[3,4,5,6,1,2] if it was rotated 4 times.

．[1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]
Output: 1

Example 2:

Input: nums = [4,5,0,1,2,3]
Output: 0

Example 3:

Input: nums = [4,5,6,7]
Output: 4

Constraints:

．1 <= nums.length <= 1000

．-1000 <= nums[i] <= 1000

=============================================================================

**UMPIRE Method:**

**Understand**

1.目標：找到一個被旋轉過的、原本遞增排序的數組 nums 中的最小元素。

2.條件：

．數組是遞增排序後被旋轉過的（即一段遞增序列接在另一段遞增序列後面）。

．所有元素是唯一的。

3.輸入輸出示例：

．如果 nums = [4,5,6,7,0,1,2]，則輸出為 0。

．如果 nums = [3,4,5,1,2]，則輸出為 1。

**Match**

我們可以利用 二分搜尋法 來縮小搜尋範圍，達成 O(log n) 的效率。

**Plan**

1.設定兩個指標 left 和 right，分別指向數組的開頭和結尾。

2.進入一個循環，當 left < right 時：
．計算中間索引 mid。
．比較 nums[mid] 和 nums[right] 的值：
  ．如果 nums[mid] 比 nums[right] 大，表示最小值在右半部分（包括 mid 右側的元素）。
    ．將 left 設為 mid + 1。
  ．否則，表示最小值在左半部分或 mid 本身。
    ．將 right 設為 mid。
3.當 left 與 right 重合時，此位置即為最小元素的位置，返回 nums[left]。

**Implement**

see solution.py

**Review**

1.檢查邊界條件：

．數組只有一個元素時應該可以正確處理，會直接返回該元素。

．若數組未被旋轉（例如 [1, 2, 3, 4]），也可以找到最小元素。

2.效率：每次迭代中，搜尋範圍減半，因此時間複雜度為 O(log n)。

**Evaluate**

這段程式碼應該能有效地在最小的時間內找到最小值。



