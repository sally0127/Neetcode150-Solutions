**Subsets**
-

🔗 Link: Subsets

💡 Difficulty: Medium

🛠️ Topics: Backtracking (回溯法) 、遞歸樹的結構、迭代與回溯的比較、位運算的應用、組合數學 (Combinatorics)

===========================================

Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [7]

Output: [[],[7]]

Constraints:

．1 <= nums.length <= 10

．-10 <= nums[i] <= 10

===================================================

**UMPIRE Method:**

**Understand**

你的理解很正確，這題確實是關於子集的生成，類似於排列組合的思考方式，但這裡的重點是生成所有子集而不是排列，順序並不重要。

1.輸入：

．一個由唯一整數組成的數組 nums。

2.輸出：

．返回所有可能的子集。

3.限制條件：

．子集不能有重複的數字。

．不需要按照特定順序返回子集。

4.特點：

．子集包含空集和完整的數組本身。

．可以使用回溯法或位運算等方法。

範例：

Input: nums = [1,2,3]

Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

**Match**

這題可以匹配到以下模式：

1.回溯法 (Backtracking)：

    ．遞歸產生所有子集。
    
    ．動態決策是否加入某元素。

2.位運算 (Bitmask)：

    ．每個子集可以看作數組中每個數是否被選中，對應到二進位的每一位。

3.迭代法 (Iterative)：

    ．每次對現有的子集新增一個新數字以產生更多子集。

**Plan**

我們選擇回溯法，因為它直觀且易於實現。

步驟：

1.初始化結果列表 res 為空，並定義回溯函數。

2.從數組的第0個元素開始，對每個元素進行兩個選擇：

    ．選擇該元素，加入當前子集。
    
    ．不選擇該元素，跳過。

3.將當前生成的子集加入結果列表。

4.遞歸遍歷剩餘元素。

5.返回結果列表。

**Implement**

see solution.py

**Review**

檢查重要案例：

1.空數組： nums = [] => 輸出 []

2.單元素： nums = [1] => 輸出 [[], [1]]

3.一般情況： nums = [1,2,3] => 輸出 [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

**Evaluate**

1.時間複雜度： O(2*n⋅n)，其中 n 是 nums 的長度。原因是：

．2 *n是所有可能的子集數量。

．每個子集平均需要 O(n) 的時間來複製。

2.空間複雜度： O(n)，遞歸棧的深度。



