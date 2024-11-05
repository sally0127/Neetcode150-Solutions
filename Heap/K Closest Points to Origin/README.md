**K Closest Points to Origin**
-
🔗 Link: K Closest Points to Origin

💡 Difficulty: Medium

🛠️ Topics: 堆（Heap）、優先隊列（Priority Queue）、幾何距離計算、時間與空間效率、資料結構的選擇

=========================================

You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:

Input: points = [[0,2],[2,2]], k = 1
Output: [[0,2]]

Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:

Input: points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]

Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:

．1 <= k <= points.length <= 1000

．-100 <= points[i][0], points[i][1] <= 100

=============================================================

**UMPIRE Method**

**Understand**

1.問題：給定一組 2D 平面的點座標陣列 points 和一個整數 k，要求找出距離原點 (0, 0) 最近的 k 個點。

2.距離定義：使用歐幾里得距離公式，即 距離= √(x−0)**2+(y−0)**2，但是我們不需要真正取平方根，因為距離的比較可以用平方來簡化。

3.輸出：返回距離原點最近的 k 個點，可以是任意順序。

4.邊界情況:

．如果 k 等於 points 的長度，那麼直接返回所有點。

．如果 points 為空或 k 為 0，則應返回空列表。

**Match**

1.計算距離並儲存：可以計算每個點到原點的距離（不取平方根）並儲存這些值。

2.使用最大堆（Max-Heap）：因為我們希望找出距離最小的 k 個點，所以我們可以使用最大堆來存儲距離與點的配對，並將最大堆的大小限制為 k。

    ．如果當前堆的大小已滿 k 且新點的距離小於堆頂（即堆中的最大值），則彈出堆頂並插入新點，保持堆中始終為最接近的 k 個點。

**Plan**

1.初始化最大堆：將堆的大小設為 k。

2.遍歷點座標：對於每個點 (x, y) 計算其距離的平方 dist = x^2 + y^2。

    ．如果堆中元素少於 k 個，將當前點推入堆。
    
    ．如果堆已滿且新點的距離小於堆頂點的距離，則彈出堆頂並插入新點。

3.返回結果：遍歷完成後，堆中保留的就是距離最小的 k 個點。返回堆中所有的點作為結果。

**Implement**

see solution.py

**Review**

1.正確性：檢查代碼，確認使用最大堆的方式來追蹤最近的 k 個點是正確的。

2.邊界檢查：覆核邊界條件，例如當 k = 0、k 等於 points 長度、或 points 為空時的行為。

3.時間複雜度：

    ．對於每個點，我們計算距離並對堆進行操作，因此時間複雜度為 O(nlogk)，其中 n 是 points 的數量，k 是所需的最近點數。

**Evaluate**

1.時間複雜度：O(nlogk)，對於每個點的插入和替換操作來說，這樣的複雜度是相對高效的。

2.空間複雜度：O(k)，因為我們最多儲存 k 個點。


