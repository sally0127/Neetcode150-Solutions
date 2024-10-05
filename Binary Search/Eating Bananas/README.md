**Eating Bananas**
-
🔗 Link: Eating Bananas

💡 Difficulty:Medium

🛠️ Topics:Binary Search (二分搜尋),Greedy Algorithm (貪心算法),Mathematical Optimization (數學優化)

===============================================================

You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:

Input: piles = [1,4,3,2], h = 9
Output: 2

Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:

Input: piles = [25,10,23,4], h = 4
Output: 25

Constraints:

．1 <= piles.length <= 1,000

．piles.length <= h <= 1,000,000

．1 <= piles[i] <= 1,000,000,000

======================================================================

**UMPIRE Method:**

**Understand**

我們需要做的是：

  ．給定一組香蕉堆 piles 和總時間 h。
  
  ．找出一個最小的吃香蕉速度 k，使得能在 h 小時內吃完所有香蕉。
  
關鍵規則：

．每小時你可以從其中一堆裡選擇 k 根香蕉來吃。如果該堆的香蕉數量少於 k，你會吃完該堆，但不能在同一小時內吃其他堆的香蕉。

．我們要求在 h 小時內吃完所有香蕉，並找到能滿足這個條件的最小 k。

需要理解的問題：

  1.給的香蕉堆 piles 的長度是多少？
  
  2.每小時的吃香蕉速度 k 最小是多少，最大又是多少？（最小是1，最大是堆裡香蕉數的最大值）
  
  3.我們需要保證能在 h 小時內吃完，所以總時間的計算方式是甚麼？

**Match**

這是一道經典的「最優化問題」，我們可以用 二分搜尋法 來尋找最小的 k。為什麼？因為香蕉吃的速度 k 有一個下限和上限，我們可以在這範圍內進行搜尋。

**Plan**

我們的目標是用二分搜尋法找到最小的 k，讓我們在 h 小時內吃完所有香蕉。具體步驟如下：

1.設定初始範圍：

．最小速度 k_min = 1。

．最大速度 k_max = max(piles)（即所有香蕉堆中最大的香蕉數量）。

2.使用二分搜尋來找出最小的 k：

．每次取中間值 mid 作為 k。

．計算在這個速度下，吃完所有香蕉需要的總時間。

．如果總時間超過 h，說明 k 太小，需要增大速度；如果總時間在 h 小時以內，則減小 k 試試更小的速度。

3.最後返回能滿足條件的最小 k。

**Implement**

see solution.py

**Review**

檢查邏輯，看看是否正確實現了最小的 k，且在給定的 h 小時內能吃完所有香蕉。

**Evaluate**

．時間複雜度：O(log(max(piles)) * n)，其中 n 是 piles 的長度。

．空間複雜度：O(1)。



