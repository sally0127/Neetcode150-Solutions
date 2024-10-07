**Time Based Key-Value Store**
-
🔗 Link: Time Based Key-Value Store

💡 Difficulty: Medium

🛠️ Topics: Data Structures (數據結構),Binary Search (二分搜尋法),Time Complexity (時間複雜度),Handling Timestamps (時間戳的處理),Key-Value Storage (鍵值存儲)

================================================================

Implement a time-based key-value data structure that supports:

．Storing multiple values for the same key at specified time stamps.

．Retrieving the key's value at a specified timestamp.

Implement the TimeMap class:

．TimeMap() Initializes the object.

．void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.

．String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".

Note: For all calls to set, the timestamps are in strictly increasing order.

Example 1:

Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:

TimeMap timeMap = new TimeMap();

timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.

timeMap.get("alice", 1);           // return "happy"

timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.

timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.

timeMap.get("alice", 3);           // return "sad"

Constraints:

．1 <= key.length, value.length <= 100

．key and value only include lowercase English letters and digits.

．1 <= timestamp <= 1000

=========================================================================

**UMPIRE Method:**

**Understand**

1.TimeMap初始化物件:

．使用 TimeMap 類來創建一個時間基礎的鍵值數據結構。

2.儲存 key, value 在特定的 timestamp:

．使用 set(key, value, timestamp) 方法來儲存鍵和對應的值以及時間戳。

3.檢索 value 在特定的 timestamp:

．使用 get(key, timestamp) 方法來檢索在給定時間戳下最接近的鍵的值，如果存在的話。

**Match**

．使用字典（或 defaultdict）來存儲每個鍵的值和對應的時間戳。

．對於每個鍵，使用一個列表來保存所有的值和時間戳對。這樣可以快速檢索到時間戳之前的值。

**Plan**

1.初始化 TimeMap 類:

．定義一個字典來存儲所有的鍵及其對應的值和時間戳的列表。

2.set 方法:

．將傳入的 key、value 和 timestamp 儲存到字典中，時間戳列表應為嚴格遞增的，確保能夠正確檢索。

3.get 方法:

．對於給定的 key，檢查其是否存在，如果存在，使用二分搜尋法找到在 timestamp 時間戳之前的最大值。

**Implement**

see solution.py

**Review**

1.測試 set 方法:

．確保能夠正確地將值和時間戳存儲到字典中。

2.測試 get 方法:

．確保能夠根據給定的時間戳正確返回最接近的值。

．檢查不存在的鍵或時間戳情況是否能返回正確結果。

**Evaluate**

．時間複雜度:
  
  ．set 方法為 O(1)，因為只是向列表添加元素。
  
  ．get 方法為 O(log n)，因為使用了二分搜尋法來查找時間戳。

．空間複雜度為 O(n)，因為需要儲存所有的鍵值對。




