**Last Stone Weight**
-
🔗 Link: Last Stone Weight

💡 Difficulty: Easy

🛠️ Topics: 堆（Heap）資料結構、優先佇列（Priority Queue）、模擬步驟、時間與空間複雜度考量

============================================

You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them together

If x == y, both stones are destroyed

If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:

Input: stones = [2,3,6,2,4]
Output: 1

Explanation:

We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].

We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].

We smash 2 and 2, so the array becomes [1].

Example 2:

Input: stones = [1,2]
Output: 1

Constraints:

．1 <= stones.length <= 20

．1 <= stones[i] <= 100

===================================================

**UMPIRE Method:**

**Understand**

1.操作：每次挑出兩顆最重的石頭 x 和 y 進行比較。如果兩顆石頭重量相等，則兩者都被摧毀；如果 x<y，則 x 被摧毀，y 的新重量變為 y−x。

2.結束條件：當只剩下一顆或零顆石頭時，結束模擬。

3.輸出：返回剩餘的石頭重量；如果沒有石頭剩下，返回 0。

**Match**

1.使用最大堆（Max-Heap），以便每次可以在 O(logn) 的時間複雜度內找到並移除兩顆最重的石頭。

2.因為 Python 中默認只有最小堆，這裡可以通過將石頭重量存為負數來實現最大堆效果。

**Plan**

以下是解決步驟：

1.初始化最大堆：將 stones 中所有石頭的重量轉為負數（模擬最大堆），然後加入堆。

2.模擬過程：

  ．當堆中元素數量大於 1 時，重複以下操作：

    ．移除並取出堆中的兩個最重石頭（由於是最大堆，我們取出的實際是兩個最小的負數）。
    
    ．如果兩個石頭重量相等，兩個石頭都摧毀。
    
    ．如果不相等，計算剩下的重量（y - x），並將其轉為負數再加入堆中。

3.結束和返回：最後，檢查堆中是否還有石頭。如果有，返回堆頂石頭的正值；否則，返回 0。

**Implement**

see solution.py

**Review**

使用範例進行測試以確保程式的正確性。例如：

1. **測試範例**：`stones = [2, 7, 4, 1, 8, 1]`

   - 步驟：

     1. 初始堆：`[8, 7, 4, 2, 1, 1]`（其實是 `[-8, -7, -4, -2, -1, -1]` 的形式）

     2. 取出 `8` 和 `7`：`8 - 7 = 1`，堆變成 `[4, 2, 1, 1, 1]`

     3. 取出 `4` 和 `2`：`4 - 2 = 2`，堆變成 `[2, 1, 1, 1]`

     4. 取出 `2` 和 `1`：`2 - 1 = 1`，堆變成 `[1, 1, 1]`

     5. 取出 `1` 和 `1`：兩顆石頭都摧毀，堆變成 `[1]`

   - 結果：堆中剩下的唯一石頭重量為 `1`。

2. **單一石頭的情況**：`stones = [1]`

   - 初始堆：`[1]`，直接返回 `1`。

3. **所有石頭重量相等**：`stones = [2, 2, 2, 2]`

   - 每次取出兩顆重量相等的石頭，它們都會被摧毀。

   - 結果：最終剩下 `0`，因為所有石頭都被摧毀。

這些測試案例幫助確認程式是否在不同情況下（包括一般情況、邊界情況等）能正常運行。

**Evaluate**

．時間複雜度：每次操作需要從堆中移出兩個元素並加入新元素，因此每次迭代的時間複雜度為 O(logn)。最多進行 O(n) 次操作，因此整體時間複雜度為O(nlogn)。

．空間複雜度：我們使用了一個堆來儲存石頭，因此空間複雜度為 O(n)。





