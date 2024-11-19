**Combination Sum**
-
🔗 Link: Combination Sum

💡 Difficulty: Medium

🛠️ Topics: 回溯法 (Backtracking)、組合數學 (Combinatorics)、遞歸樹 (Recursive Tree)、剪枝 (Pruning)

=====================================

You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Example 1:

Input: 
nums = [2,5,6,9] 
target = 9

Output: [[2,2,5],[9]]

Explanation:
2 + 2 + 5 = 9. We use 2 twice, and 5 once.
9 = 9. We use 9 once.

Example 2:

Input: 
nums = [3,4,5]
target = 16

Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

Example 3:

Input: 
nums = [3]
target = 5

Output: []

Constraints:

．All elements of nums are distinct.

．1 <= nums.length <= 20

．2 <= nums[i] <= 30

．2 <= target <= 30

=============================================

**UMPIRE Method:**

**Understand**

題目分析：

1.輸入：

    ．一個整數數組 nums（所有數字均為顯著的正整數）。
    
    ．一個整數 target，表示目標值。

2.輸出：

    ．返回所有可能的組合，每個組合的數字加總等於 target。
    
    ．每個數字可以被多次使用。

3.條件限制：

    ．數字的排列順序不影響結果。
    
    ．組合必須是唯一的（例如 [2, 2, 3] 和 [3, 2, 2] 視為相同）。
    
    ．如果沒有解，返回空列表。

題目例子：

．nums = [2, 3, 6, 7], target = 7

    ．輸出：[[7], [2, 2, 3]]

．nums = [2, 3, 5], target = 8

    ．輸出：[[2, 2, 2, 2], [2, 3, 3], [3, 5]]

．nums = [2], target = 1

    ．輸出：[]

理解關鍵：

．回溯法是一種有效解決此問題的方式，因為：

    1.我們需要生成所有可能的組合。
    
    2.允許重複選擇，適合在遞歸過程中多次嘗試同一個數字。
    
    3.剪枝優化避免不必要的探索（當目標值變小於 0 時停止）。
    
**Match**

這題的核心點在於找到符合條件的所有組合，匹配的技巧包括：

1.回溯法 (Backtracking)

    ．適合處理「找出所有可能的解」的問題，例如排列組合、子集生成等。
    
    ．可以動態選擇數字並進行剪枝，避免重複計算。

2.組合數學 (Combinatorics)

    ．處理如何選擇數字，使得總和等於目標值。
    
    ．包含順序無關的唯一性處理（從索引 start 開始遞歸，避免重複組合）。
 
 3.遞歸樹 (Recursive Tree)

    ．問題可以被視為一棵遞歸樹，每一層代表選擇數字的決策。
    
    ．深度優先搜索 (DFS) 適合用來遍歷所有可能的路徑。

4.剪枝 (Pruning)

    ．當剩餘目標值 (remaining) 小於 0 時停止遞歸，避免無意義的運算。
    
    ．提升效率，減少不必要的運算路徑。

**Plan**

使用 Backtracking 的解法：

1.初始化： 定義一個結果列表 res 用來存儲所有符合條件的組合。

2.回溯函數設計：

  ．輸入參數包括當前索引 start（避免重複選擇更前面的數字）、當前組合 path 和剩餘目標 remaining。
  
  ．終止條件：

      ．當 remaining == 0 時，表示找到一組組合，將其加入結果列表。
      
      ．當 remaining < 0 時，剪枝返回，因為不可能達成目標。

  ．遞歸選擇：

    ．從當前索引 start 開始遍歷 nums。
    
    ．選擇當前數字，加入 path，並繼續遞歸（允許重複選擇，所以遞歸時索引仍是 start）。

    ．回溯時移除剛剛選擇的數字。

3.返回結果： 最終返回結果列表 res。

**Implement**

see solution.py

**Review**

檢查重要案例：

1.空數組或無解： nums = [2,3,6,7], target = 1 => 輸出 []

2.有解情況：

    ．nums = [2,3,6,7], target = 7 => 輸出 [[7], [2,2,3]]
    
    ．nums = [2,3,5], target = 8 => 輸出 [[2,2,2,2], [2,3,3], [3,5]]

**Evaluate**

1.時間複雜度： O(2**t)，其中 t=target / min(nums)，因為每次選擇可能導致兩個分支。

2.空間複雜度： O(t)，為遞歸棧的深度。

3.優點： 直接遞歸，程式結構清晰且易於理解。

4.缺點： 如果輸入過大或目標值過高，可能會遇到性能瓶頸。

**補充**

1.

剪枝 (Pruning) 是一種在演算法中優化搜索空間的技巧，目的是減少不必要的計算，提升效率。

在解題過程中，當你確定某些選擇不可能導致目標結果時，可以直接「剪掉」這些分支，避免繼續深入計算。這樣可以大幅減少時間和空間的消耗。

2.

剪枝的基本原則
    
    1.條件篩選： 如果某些路徑或選擇無法達到目標，可以提前終止該路徑的探索。
    
    2.提前退出： 利用已知的約束條件，避免嘗試所有可能性。

3.

在這題的應用：Combination Sum

在 Combination Sum 的問題中：

    1.條件： 當剩餘的目標值 remaining 小於 0 時，表示目前的組合已經不可能達到目標值。
    
    2.剪枝動作： 在這種情況下停止遞歸，直接返回。

4.

剪枝的優點

1.減少無效路徑，節省計算資源。

2.提高程式執行速度，特別是目標值很大時效果明顯。

3.將重心集中於有潛力達成目標的分支。

總結

剪枝 就是「果斷放棄無意義的分支」，是演算法中的一種核心優化策略，在這類問題中非常重要！

