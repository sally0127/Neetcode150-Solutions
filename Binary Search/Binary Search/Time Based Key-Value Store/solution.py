from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.store =  defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the value and timestamp to the list for this key
        self.store[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return""

        # Get the list of (timestamp, value) pairs for the key
        values = self.store[key]


        # Binary search to find the rightmost value with timestamp <= given timestamp
        idx = bisect.bisect_right(values,(timestamp,chr(255)))


        if idx == 0:
            return ""

        return values[idx - 1][1]


================================================================================

**這題的偽代碼可以分為 set 和 get 兩個部分，重點在於利用時間戳排序的特性來有效地查找和插入。以下是偽代碼：**

  class TimeMap:
    
    Initialize data structure:
    - store: A dictionary to hold each key with a list of (timestamp, value) pairs.
    
    Method: set(key, value, timestamp)
    - If key is not in store:
        - Add a new empty list for this key in store.
    - Append the (timestamp, value) pair to store[key].

    Method: get(key, timestamp)
    - If key is not in store:
        - Return an empty string "" since there's no entry for this key.
        
    - Retrieve the list of (timestamp, value) pairs for the key.
    - Perform binary search on the list to find the largest timestamp that is ≤ given timestamp.
        - If no valid timestamp is found (all are greater than the given timestamp):
            - Return "".
        - Else:
            - Return the `value` associated with the found timestamp.

更詳細的說明

1.set 方法

．每次調用時，把 (timestamp, value) 加入對應 key 的列表。由於時間戳是遞增的，無需排序。

2.get 方法

．利用二分搜索找到不大於輸入 timestamp 的最近時間戳的 value。
