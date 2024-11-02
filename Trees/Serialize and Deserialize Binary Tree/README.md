**Serialize and Deserialize Binary Tree**
-
🔗 Link: Serialize and Deserialize Binary Tree

💡 Difficulty: Hard

🛠️ Topics: 樹的序列化和反序列化、遍歷方法、遞迴和堆疊的使用、時間複雜度和空間複雜度

===========================================

Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:

Input: root = []
Output: []

Constraints:

．0 <= The number of nodes in the tree <= 1000.

．-1000 <= Node.val <= 1000

========================================================

**UMPIRE Method:**

**Understand**

．目標：實現一個算法，將二元樹序列化為字串，並能夠從這個字串反序列化回原始的二元樹結構。

．輸入：一個二元樹的根節點。

．輸出：序列化後的字串，以及從字串反序列化後的二元樹根節點。

**Match**

1.序列化：使用前序遍歷（根-左-右）來遍歷樹，將每個節點的值儲存到字串中，並用特殊符號（如#）來表示空節點。

2.反序列化：根據序列化時產生的字串，使用前序遍歷的順序重建樹結構。

**Plan**

1.確定序列化格式：

    ．決定使用前序遍歷來序列化二元樹。選擇前序遍歷是因為它能夠在遍歷的過程中直接獲得根節點，並且容易將其轉換成字串。
    
    ．使用#符號表示空節點，以便能夠在反序列化時區分出缺失的子樹。

2.編寫序列化函數：

    ．實現serialize(root)函數，該函數接收樹的根節點並返回序列化的字串。

    ．在函數內部，使用遞迴進行前序遍歷，將每個節點的值和#符號拼接成一個字串。

3.編寫反序列化函數：

    ．實現deserialize(data)函數，該函數接收序列化的字串並返回重建的二元樹根節點。
    
    ．在函數內部，使用split方法將字串轉換為一個值的列表，然後使用遞迴來重建樹，依據前序遍歷的順序進行操作。

4.測試功能：

    ．編寫測試案例來檢查序列化和反序列化的正確性，特別注意邊界情況，如空樹、只有一個節點的樹等。
    
    ．確認序列化的結果可以正確反序列化回原來的樹結構。

5.時間與空間複雜度分析：

    ．在完成實現後，進行時間和空間複雜度的分析，並考慮在不同情況下（如極大或極小的樹）性能的變化。

**Implement**

see solution.py

**Review**

確保測試包括邊界情況，如空樹和只有一個節點的樹，並確認序列化的結果可以正確反序列化回原來的樹結構。

**Evaluate**

．時間複雜度：序列化和反序列化的時間複雜度都是O(n)，其中n是樹中節點的數量，因為需要遍歷每個節點。

．空間複雜度：序列化過程中的字串儲存空間也是O(n)，而在反序列化過程中，遞迴的堆疊空間最壞情況下也是O(n)。
