**Subsets II**
-

🔗 Link: Subsets II

💡 Difficulty: Medium

🛠️ Topics: 回溯 (Backtracking)、排序與去重 (Sorting and Deduplication)、子集生成 (Subset Generation)、遞歸與分治思想 (Recursion and Divide & Conquer)

======================================

You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]

Constraints:

．1 <= nums.length <= 11

．-20 <= nums[i] <= 20

====================================================

**UMPIRE Method:**

**Understand**

1.What is the input?

  ．一個整數數組 nums，可能包含重複的元素。

2.What is the output?

  ．所有可能的子集，每個子集不包含重複且不重複出現。

3.Clarify ambiguities:

  ．是否需要按照特定順序返回子集？

    ．答案： 不需要，任意順序皆可。

  ．子集是否可以是空集？

    ．答案： 可以，空集是有效子集。

**Match**

使用 Backtracking 是解決此問題的有效方式，因為：

1.nums 可能包含重複的元素，這會導致常規子集生成方法產生重複的子集。

2.通過先排序 nums，並在遞歸過程中跳過相鄰重複的元素，我們可以有效避免生成重複子集。

**Plan**

1.Sort the array:

  ．將 nums 排序，方便處理重複的元素。

2.Use a backtracking function:

  ．構建遞歸函數 backtrack(start, path)，其中：

    ．start 是當前遞歸的起始索引。

    ．path 是目前生成的子集。

3.Add subsets to the result list:

  ．每次呼叫遞歸時，將 path 添加到結果中。

4.Avoid duplicates:

  ．在遞歸中，若當前元素與上一個元素相同且上一個元素尚未使用，則跳過當前元素。

5.Base case:

  ．遞歸終止於所有元素被處理完畢。

**Implement**

see solution.py

**Review**

1.檢查正確性：

    ．排序 nums 後，重複元素跳過邏輯：if i > start and nums[i] == nums[i - 1]。
    
    ．Backtracking 遞歸包含「選擇、探索、撤銷選擇」三步，無邏輯錯誤。
    
    ．用例檢查如 nums = [1, 2, 2] 和 nums = []，結果正確。

2.邏輯與邊界條件：

    ．空數組、全重複元素的數組處理正確。

**Evaluate**

1.時間與空間複雜度：

．時間：O(N log N + 2^N)，排序 + 子集生成。

．空間：O(N)，遞歸堆疊深度與當前子集 path。

2.優缺點：

．優點： 邏輯清晰，避免重複子集，適合中小數組。

．缺點： 隨 N 增加，時間複雜度快速增長。
