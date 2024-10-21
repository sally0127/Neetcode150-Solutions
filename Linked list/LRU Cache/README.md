**LRU Cache8**
-
🔗 Link: LRU Cache8
💡 Difficulty: Medium
🛠️ Topics: 缓存淘汰策略(Cache Eviction Policy),数据结构设计 (Data Structure Design),算法优化(Algorithm Optimization),缓存管理(Cache Management)

=============================================

Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

．LRUCache(int capacity) Initialize the LRU cache of size capacity.

．int get(int key) Return the value cooresponding to the key if the key exists, otherwise return -1.

．void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Example 1:

Input:

["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

Output:

[null, null, 10, null, null, 20, -1]

Explanation:

LRUCache lRUCache = new LRUCache(2);

lRUCache.put(1, 10);  // cache: {1=10}

lRUCache.get(1);      // return 10

lRUCache.put(2, 20);  // cache: {1=10, 2=20}

lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted

lRUCache.get(2);      // returns 20 

lRUCache.get(1);      // return -1 (not found)

Constraints:

．1 <= capacity <= 100

．0 <= key <= 1000

．0 <= value <= 1000

======================================================

**UMPIRE Method:**

**Understand**

．目标：创建一个 LRU 缓存，该缓存支持 get(key) 和 put(key, value) 操作，并且都要求在 O(1) 时间复杂度内完成。

．重要信息：

    ．容量限制：缓存容量有限，如果超过容量，应该移除最少最近使用的元素。
    
    ．操作细节：
    
      ．get(key)：如果键存在，返回对应的值，并将其标记为最近使用。
      
      ．put(key, value)：插入新的键值对，如果缓存已满，移除最少最近使用的键。

**Match**

．这是典型的 缓存淘汰问题，常见解决方案是使用 哈希表 和 双向链表 来确保在 O(1) 时间内完成 get 和 put 操作。

．哈希表：用于快速查找键值对，保证 get 的时间复杂度为 O(1)。

．双向链表：用于维护使用顺序，最近使用的元素放在链表头，最少使用的元素放在链表尾部。

．缓存淘汰策略：使用 LRU（Least Recently Used），每次访问（get 或 put）都将元素移动到链表头部，满容量时删除尾部的节点。

**Plan**

．初始化 LRUCache：

  ．设定缓存容量，创建一个双向链表用于存储使用顺序，同时使用哈希表保存 key 到链表节点的映射。

．get 操作：

  ．在哈希表中查找 key 是否存在。如果存在，将该节点移动到链表头部，并返回其值。如果不存在，返回 -1。

．put 操作：

  ．如果 key 存在，更新其值，并将该节点移动到链表头部。
  
  ．如果 key 不存在，插入新的键值对到链表头部。如果缓存已满，删除链表尾部节点并从哈希表中移除对应的键。

**Implement**

see solution.py

**Review**

．代码逻辑符合 LRU 缓存的要求，每个操作都在 O(1) 时间复杂度内完成。

．使用哈希表和双向链表相结合保证了高效的查找和更新操作。

．进一步确认逻辑是否存在边界问题（如容量为 0 或插入相同键值等）。

**Evaluate**

．测试场景：缓存满时是否正确删除最少使用的节点。

．边界情况：缓存容量为 1 时、反复 get 操作时的行为等。

