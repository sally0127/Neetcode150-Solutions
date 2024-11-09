**Task Scheduling**
-
🔗 Link: Task Scheduling

💡 Difficulty: Medium

🛠️ Topics: 任務頻率分析、最大頻率任務優先、冷卻時間（空閒時間）、最小化總排程時間、空閒時間的填補

[!NOTE]

這題考察的主要觀念是**任務排程與冷卻時間管理**，具體來說是如何在有限的 CPU 週期內，遵循相同任務之間必須有至少 n 單位時間的冷卻時間，並且最小化總的 CPU 週期。這考驗了對排程問題的理解與優化，以及如何有效計算「空閒時間」（idle time）來滿足冷卻條件。

====================================

You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2
Output: 5

Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3
Output: 9

Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

Constraints:

．1 <= tasks.length <= 1000

．0 <= n <= 100

===============================================

**UMPIRE Method**

**Understand**

．給定一組任務 tasks，每個任務都是一個大寫字母，表示不同的工作。

．相同任務之間必須至少間隔 n 個 CPU 週期，以滿足冷卻需求。

．每個 CPU 週期只能執行一項任務，或讓 CPU 處於空閒。

．目標：找出完成所有任務所需的 最小 CPU 週期數。

**Match**

．這是一個「任務排程」的問題，我們需要最小化時間並滿足「相同任務冷卻」的限制。

．計算每個任務的頻率，找到出現最多的任務作為參考，再依此安排週期，滿足冷卻條件。

**Plan**

．計算各任務的頻率，找到出現次數最多的任務（max_freq）。

．找到具有此最高頻率的任務數量（count_of_max_freq）。

．使用公式來計算最少的週期數：

    ．((max_freq - 1) * (n + 1) + count_of_max_freq)。
    
    ．取此結果和任務總數的較大值以覆蓋所有任務。

**Implement**

see solution.py

**Review**

．檢查邏輯是否正確地滿足冷卻間隔。

．確認所有任務都有適當排程，沒有遺漏。

．確認公式的計算步驟符合計劃。

**Evaluate**

．時間複雜度：O(N)，其中 N 是任務數量。

    ．使用 Counter 計算任務頻率需要 O(N)。
    
    ．找出 max_freq 和計算 max_freq_tasks 也需要 O(N)。
    
    ．整體來說，此解法在任務數目增加時仍具有良好的表現。

．空間複雜度：O(1)，如果我們只考慮固定大小的字母數量 (A-Z)。

    ．Counter 的大小取決於任務的種類數量 (最多 26 個英文字母)，屬於常數級別。

