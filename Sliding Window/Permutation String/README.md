**Permutation String**
-
🔗 Link: Permutation String

💡 Difficulty: Medium

🛠️ Topics: 滑動窗口（Sliding Window）,頻率計數（Frequency Counting）,排列組合（Permutations）,字串匹配（String Matching）,時間與空間複雜度（Time and Space Complexity）

==========================================================

You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"
Output: true

Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"
Output: false

Constraints:

．1 <= s1.length, s2.length <= 1000

============================================================================

**UMPIRE Method:**

**Understand**

1.給定兩個字串 s1 和 s2。

2.判斷 s2 是否包含 s1 的排列組合作為子字串。

3.如果 s2 包含 s1 的排列組合作為子字串，回傳 true，否則回傳 false。

4.所有字元皆為小寫字母。

**Match**

這題適合用 Sliding Window 和 Hash Table（或者頻率計數）來處理，因為我們可以使用固定大小的窗口來檢查 s2 是否包含 s1 的排列。

**Plan**

1.計算字符頻率：首先，創建一個字母頻率的字典，記錄 s1 中各字符的出現次數。

2.初始化窗口：使用兩個指針 left 和 right 構成一個窗口，窗口大小應該等於 s1 的長度。

3.滑動窗口檢查：

．移動 right 指針來增加窗口字符，並更新窗口內字符的頻率計數。

．當窗口大小達到 s1 的長度時，檢查該窗口的字符頻率是否和 s1 的頻率字典匹配。如果匹配則返回 true。

．如果頻率不匹配，則將 left 向右移動以縮小窗口，並更新頻率。

4.返回結果：若遍歷完 s2 仍沒有匹配的子字串，則返回 false。

**Implement**

see solution.py

**Review**

1.效率：這個方法使用滑動窗口和頻率計數，時間複雜度為 O(n)，空間複雜度為 O(1)，因為最多只需計算 26 個字母的頻率。

2.邊界情況：確認 s1 長度大於 s2 時返回 false。若 s1 或 s2 為空字串，應根據題目要求的情況決定如何處理。

**Evaluate**

測試用例：

．check_inclusion("ab", "eidbaooo") 應返回 True

．check_inclusion("ab", "eidboaoo") 應返回 False


