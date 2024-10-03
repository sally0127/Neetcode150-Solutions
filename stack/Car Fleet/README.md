**Car Fleet**
-
🔗 Link: Car Fleet(https://neetcode.io/problems/car-fleet)

💡 Difficulty: Medium

🛠️ Topics: Stack (堆疊),Sorting(排序),Greedy (貪心算法)

===============================================================

There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.

Example 1:

Input: target = 10, position = [1,4], speed = [3,2]
Output: 1

Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

Example 2:

Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
Output: 3

Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

Constraints:

．n == position.length == speed.length.

．1 <= n <= 1000

．0 < target <= 1000

．0 < speed[i] <= 100

．0 <= position[i] < target

．All the values of position are unique.

=======================================================================

**UMPIRE Method:**

**Understand**

1.基本規則：

．後面的車不能超過前面的車。

．如果一輛車追上前面的車，它們會成為同一個車隊，並以相同的速度到達終點。

．回傳最終有多少個不同的車隊。

2.邊界條件：

．位置可以為 0（初始位置）。

．如果車輛無法追上前面的車，它們將形成新的車隊。

**Match**

1.關鍵工具：使用堆疊來追蹤車輛的到達時間。當一輛車追上前面的車，兩者會組成一個車隊。

2.計算每輛車到終點的時間：這可以透過公式 (target - position[i]) / speed[i] 計算，這個公式是整個問題的核心，用來判斷車輛是否能追上或超過其他車輛並合併成車隊。

3.將每輛車按位置排序：按車輛距離終點的遠近進行排序，從距離終點最近的車輛開始計算。

4.車隊的判定：

．逐一處理車輛，計算它們到達終點的時間。

．如果一輛車的到達時間比當前車隊的時間更長，則它將形成新的車隊；否則，它會加入前面的車隊。

**Plan**

1.初始化變數：設置終點 (target)、車輛數量 (n)、位置和速度的數組 (position 和 speed)。

2.計算並比較每輛車到達終點的時間：根據上面的公式計算每輛車的時間，並將車輛按照位置進行排序。

3.使用堆疊來判斷車隊：當後面車輛的到達時間比前車隊的時間長時，形成一個新的車隊。

**Implement**

see solution.py

**Review**

．測試不同的情況，如 n = 1 或多輛車速度不同的情況。

．優化計算的效率，確保在大數據下表現良好。

**Evaluate**

．評估解決方案的時間複雜度。由于我們需要遍歷每輛車並計算到達終點的時間，最壞情況下的時間複雜度應為 O(n log n)（由於排序的原因）。



