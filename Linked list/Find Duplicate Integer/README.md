**Find Duplicate Integer**
-
🔗 Link:Find Duplicate Integer

💡 Difficulty: Medium

🛠️ Topics: 鏈結串列循環檢測（Cycle Detection in Linked List）,快慢指針（Fast and Slow Pointer/Floyd's Tortoise and Hare Algorithm）.空間效率的優化

====================================================

You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Example 1:

Input: nums = [1,2,3,2,2]
Output: 2

Example 2:

Input: nums = [1,2,3,4,4]
Output: 4

Follow-up: Can you solve the problem without modifying the array nums and using O(1) extra space?

Constraints:

．1 <= n <= 10000

．nums.length == n + 1

．1 <= nums[i] <= n

======================================================

**UMPIRE Method:**

**Understand**

．給定一個包含 n + 1 個整數的數組，每個整數範圍在 [1, n] 之間。

．數組中所有的整數都只出現一次，除了有一個數字出現了兩次或更多次。

．目標是找出這個重複出現的數字。

關鍵：不使用額外的空間，且時間複雜度為 O(n)。

**Match**

．快慢指針是一個經典的應用場景，它可以在循環的數列或結構中快速找到重複數字。

．這裡的數組可以看作是具有「隱藏循環」的鏈結串列，其中數值對應指針。數組中的每個數值指向索引，而重複數字意味著有兩條「路徑」會最終指向同一個位置，形成一個循環。

**Plan**

．步驟 1：使用快慢指針來檢測循環。

  ．初始化 slow 和 fast 指針，起點是 nums[0]。
  
  ．快指針每次走兩步 (fast = nums[nums[fast]])，慢指針每次走一步 (slow = nums[slow])。
  
  ．當兩個指針相遇時，說明有循環，這就是重複數字的位置。

．步驟 2：找到循環的起點，也就是重複數字。

  ．從頭開始將 slow 指針重置為起點，並讓快慢指針同時以一步一個節點的速度移動。當它們再次相遇時，位置就是重複數字。

**Implement**

  see solution.py

**Review**

．邊界條件：

．只有一個重複數字，因此不會有多重重複的情況。

．nums 的長度為 n + 1，範圍在 [1, n]，不存在超出範圍的數字。

．測試用例：

．nums = [1, 3, 4, 2, 2]，返回 2。

．nums = [3, 1, 3, 4, 2]，返回 3。

．nums = [1, 1]，返回 1。

**Evaluate**

．時間複雜度：O(n)，因為快慢指針都會遍歷整個數組。

．空間複雜度：O(1)，不使用額外的空間來儲存數據。

