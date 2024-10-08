**Buy and Sell Crypto**
-
🔗 Link: Buy and Sell Crypto

💡 Difficulty: Easy

🛠️ Topics: 數據結構 (Data Structures),動態編程 (Dynamic Programming),滑動窗口技術 (Sliding Window Technique),最大值和最小值的計算 (Calculation of Maximum and Minimum Values),貪心算法 (Greedy Algorithm)

====================================================

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]
Output: 6

Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]
Output: 0

Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

．1 <= prices.length <= 100

．0 <= prices[i] <= 100

=========================================================================

**UMPIRE Method:**

**Understand**

1.給定一組數列，設定第幾天NeetCoin價格是多少 

2.選擇一天購買NeetCoin且在未來的某一天賣掉它 

3.回傳最大利潤，若是不想交易則回傳0 。

**Match**

這類題目需要找出一個最小的買入價（過去最低的價錢）以及與當日價格之間的最大差值。常見的做法是使用「滑動窗口」或是「單次遍歷」來更新最低價格與最大利潤。

**Plan**

1.初始化 min_price 為極大值（例如 float('inf')），這樣它會比任何一天的價格高。

2.初始化 max_profit 為 0，這樣即使不進行任何交易也會自動返回 0。

3.遍歷價格數列 prices：

  ．更新 min_price 為當前天數中遇到的最低價格。
  
  ．計算當前天數的潛在利潤，公式為 prices[i] - min_price。
  
  ．如果潛在利潤比 max_profit 更高，則更新 max_profit。

4.最後返回 max_profit。

**Implement**

see solution.py

**Review**

這段程式碼的時間複雜度是 O(n)，因為我們只需要一次遍歷即可更新 min_price 和 max_profit。

**Evaluate**

測試幾個邊界條件：

．prices = [7,1,5,3,6,4]：應返回 5（在價格為 1 時買入，價格為 6 時賣出）。

．prices = [7,6,4,3,1]：應返回 0（沒有利潤）。

．prices = [1,2]：應返回 1（在價格為 1 時買入，價格為 2 時賣出）。

這題的邏輯主要是理解如何更新最低價格和計算可能利潤，是經典的「單次買賣最大利潤」問題。


