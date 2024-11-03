**Implement Prefix Tree**
-
🔗 Link: Implement Prefix Tree

💡 Difficulty: Medium

🛠️ Topics: 資料結構設計、字串操作和前綴處理、遞迴與樹形結構的理解、時間與空間複雜度分析

=====================================
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

    ．PrefixTree() Initializes the prefix tree object.
    
    ．void insert(String word) Inserts the string word into the prefix tree.
    
    ．boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
    
    ．boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:

Input: 
["Trie", "insert", "dog", "search", "dog", "search", "do", "startsWith", "do", "insert", "do", "search", "do"]

Output:
[null, null, true, false, true, null, true]

Explanation:

PrefixTree prefixTree = new PrefixTree();

prefixTree.insert("dog");

prefixTree.search("dog");    // return true

prefixTree.search("do");     // return false

prefixTree.startsWith("do"); // return true

prefixTree.insert("do");

prefixTree.search("do");     // return true

Constraints:

．1 <= word.length, prefix.length <= 1000

．word and prefix are made up of lowercase English letters.

===========================================================

**UMPIRE Method:**

**Understand**

我們需要設計一個 前綴樹 (Trie)，這是一種樹狀資料結構，用來高效地儲存和檢索字串集合中的鍵值。常見應用包括自動完成和拼字檢查。

我們要實作的操作有：

    1.Insert (插入)：將字串新增到 Trie 中。
    
    2.Search (查找)：檢查字串是否存在於 Trie 中。
    
    3.Starts With (檢查前綴)：檢查 Trie 中是否有字串以指定的前綴開頭。

**Match**

此問題是一個典型的 Trie (前綴樹) 應用案例。前綴樹的基本概念是每個節點代表一個字符，從根節點到特定節點的路徑表示該節點的前綴。前綴樹的特點是：

    ．支援字串的高效儲存和查找。
    
    ．在節點上設置「單字結尾」的標記可以幫助我們快速確認字串是否為完整單字。

**Plan**

我們將建立兩個類別：

1.TrieNode：用來定義 Trie 中的每個節點。
    
    ．每個節點包含一個字典 children，儲存下一層的子節點，鍵為字符，值為另一個 TrieNode。
    
    ．每個節點包含一個布林值 is_end_of_word，用來標記該節點是否為某個單字的結尾。

2.PrefixTree：用來定義 Trie 的主要操作方法。

    ．insert(word)：將字串逐字符插入到 Trie 中，並在最後一個字符設置 is_end_of_word 為 True。
    
    ．search(word)：檢查字串是否存在於 Trie 中，並確保該字串的最後一個字符為 is_end_of_word。
    
    ．startsWith(prefix)：檢查 Trie 中是否存在以指定前綴開頭的字串。

**Implement**

see solution.py

**Review**

檢查代碼是否正確：

1.邊界情況：

    ．空字串輸入的處理。
    
    ．插入和查找多個有相同前綴的字串。
    
    ．檢查不存在的單字或前綴。
    
    ．適用於大小寫敏感的情況（此處假設所有字串為小寫）。

2.測試用例：

    ．插入並查找相同的字串。
    
    ．插入不同的字串並查找共同前綴。
    
    ．使用不存在於 Trie 中的前綴進行 startsWith 測試。

**Evaluate**

1.時間複雜度

    ．insert(word): O(m)，其中 m 是單字的長度。我們需要遍歷單字的每個字符並在 Trie 中新增節點。
    
    ．search(word): O(m)，其中 m 是單字的長度。這需要遍歷單字的每個字符來檢查是否存在於 Trie 中。
    
    ．startsWith(prefix): O(p)，其中 p 是前綴的長度。這需要遍歷前綴的每個字符來確認它是否存在於 Trie 中。

2.空間複雜度

  空間複雜度取決於儲存的單字數量和單字的平均長度。
    
    ．每次插入一個新單字，我們可能會新增 m 個新節點（對於前綴樹的一個新分支）。
    
    ．在最壞情況下，Trie 的空間複雜度是 O(N×M)，其中 N 是插入的單字數量，M 是單字的平均長度。
    
    ．若許多單字有共同的前綴，會共享節點，從而有效降低總空間。

這樣的評估可以幫助確認我們的實作是否符合需求，並確保它的時間和空間效率。這個 Trie 實作適合於儲存和查找大量單字的應用，例如自動完成或拼字檢查系統。


