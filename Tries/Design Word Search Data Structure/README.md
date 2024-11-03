**Design Word Search Data Structure**
-
🔗 Link: Design Word Search Data Structure

💡 Difficulty: Medium

🛠️ Topics: 資料結構的選擇、遞迴思維、時間與空間複雜度分析、邏輯與條件判斷、物件導向設計、錯誤處理與邊界條件

===========================================

Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

    ．void addWord(word) Adds word to the data structure.
    
    ．bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example 1:

Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]

Output:
[null, null, null, null, false, true, true, true]

Explanation:

WordDictionary wordDictionary = new WordDictionary();

wordDictionary.addWord("day");

wordDictionary.addWord("bay");

wordDictionary.addWord("may");

wordDictionary.search("say"); // return false

wordDictionary.search("day"); // return true

wordDictionary.search(".ay"); // return true

wordDictionary.search("b.."); // return true

Constraints:

．1 <= word.length <= 20

．word in addWord consists of lowercase English letters.

．word in search consist of '.' or lowercase English letters.

============================================================

**UMPIRE Method:**

**Understand**

1.能夠將新單詞添加到資料結構中。

2.能夠檢查某個單詞是否存在，支持通配符 .，它可以匹配任意字母。

**Match**

使用 字典樹（Trie） 作為資料結構，因為它適合於字元序列的儲存和查找，特別是可以有效支持前綴查找和通配符搜索。

**Plan**

資料結構設計：
  
  1.定義一個 TrieNode 類來表示字典樹的節點。
  
      ．children: 儲存子節點的字典。
      
      ．is_end_of_word: 布爾值，用來標識這個節點是否為單詞的結尾。
  
  2.定義 WordDictionary 類來管理整個字典樹。
  
      ．addWord(word: str): 將單詞添加到字典樹中。
      
      ．search(word: str): 搜索單詞，包括處理通配符的邏輯。
      
      ．_search_in_node(word: str, node: TrieNode): 在給定的節點上進行遞迴搜索。

**Implement**

see solution.py

**Review**

．確保 addWord 方法能夠正確添加單詞並設置結尾標誌。

．確保 search 方法能夠正確處理通配符 .，並能遍歷所有可能的字符匹配。

**Evaluate**

1.時間複雜度：

    ．添加單詞：O(L)，其中 L 是單詞的長度。
    
    ．搜索單詞：最壞情況下 O(L * 26^D)，其中 D 是通配符的數量（在最壞情況下需要遍歷所有子節點）。

2.空間複雜度：O(N * L)，其中 N 是添加的單詞數量，L 是單詞的平均長度。


