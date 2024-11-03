**Search for Word II**
-
🔗 Link: Search for Word II

💡 Difficulty: Hard

🛠️ Topics: 字典樹（Trie）、回溯法（Backtracking）、剪枝（Pruning）、DFS（深度優先搜索）、集合去重（Set for deduplication）

======================================

Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:

Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]

Example 2:

Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]

Output: []

Constraints:

．1 <= board.length, board[i].length <= 10

．board[i] consists only of lowercase English letter.

．1 <= words.length <= 100

．1 <= words[i].length <= 10

．words[i] consists only of lowercase English letters.

．All strings within words are distinct.

============================================================

**UMPIRE Method**

**Understand**

1.輸入：

    ．board：一個 2D 字符網格。
    
    ．words：一個字串列表，我們需要在 board 中尋找的字。

2.輸出：從 words 中找到的字，這些字必須可以在網格中找到。

3.限制：

    ．我們只能水平或垂直移動到相鄰的格子。
    
    ．每個格子在每個字的搜索過程中只能使用一次。

4.目標：找到所有可以在網格中形成的字。

**Match**

輸入:

board = [
  ["o", "a", "a", "n"],
  ["e", "t", "a", "e"],
  ["i", "h", "k", "r"],
  ["i", "f", "l", "v"]
]
words = ["oath", "pea", "eat", "rain"]

輸出:

["oath", "eat"]

邊界情況:

    ．空的網格或空的字列表：應返回空列表。
    
    ．包含相同前綴的字：例如 "oath" 和 "oaths"，"oath" 是前綴。
    
    ．單一格子的網格：只有與此格子匹配的字才可能被找到。

**Plan**

我們將使用 回溯法 和 Trie（字典樹） 結合的方式來進行高效的字搜尋。

步驟：

1.建立 Trie：

    ．將所有單字插入 Trie。Trie 中的每條路徑代表我們需要搜尋的單字的可能前綴。

2.遍歷網格：

    ．對於網格中的每個格子，若字母是 Trie 中有效的開頭，則開始回溯搜尋。

3.回溯並剪枝：

    ．在每次遞迴呼叫中，將當前格子標記為已訪問。
    
    ．依次檢查相鄰的格子以尋找可能的單字繼續部分。
    
    ．若找到完整的單字，則將其加入結果列表中，並在 Trie 中標記已找到（避免重複）。

4.返回所有找到的單字：

    ．當所有格子的回溯結束後，返回找到的單字集合。

**Implement**

see solution.py

**Review**

1.邊界測試：測試空 board 或空 words，以及單字的不同前綴。

2.正確性檢查：檢查每個找到的單字，確保它的路徑不重疊、不使用相同的格子。

3.回溯修正：在每次搜尋結束時將 board[row][col] 還原，避免影響後續搜尋。

**Evaluate**

1.時間複雜度：

    ．Trie 構建： O(N×L)，其中 N 是單字數量，L 是平均單字長度。
    
    ．回溯搜尋：每個格子都可能啟動一個 DFS，考慮回溯和 Trie 的剪枝，效率上比純回溯要高效。

2.空間複雜度：

    ．Trie 的空間與 words 中單字的數量和長度成正比。
    
    ．回溯的遞迴深度最大為單字的長度。

