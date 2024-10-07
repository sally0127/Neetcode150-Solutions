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

        # Get the list of (timestamp, value) pairs for the key          **首先取得對應 key 的時間戳和值的列表，這個列表中的每個元素是 (timestamp, value) 的形式，並且時間戳是嚴格遞增的。**
        values = self.store[key]


        # Binary search to find the rightmost value with timestamp <= given timestamp   **bisect_right 是 Python 的 bisect 模塊中的一個方法，適用於二分查找。**                                                                                        
        idx = bisect.bisect_right(values,(timestamp,chr(255)))                          **(timestamp, chr(255)) 是用來比較的假設值：這裡 chr(255) 是一個高 ASCII 字符（最接近 255 的字符），其主要目的是確保當遇到相同 timestamp 時，這個值會放在最後。因為 values 中的 (timestamp, value) 是按照時間戳排序的。
                                                                                        **最終，bisect_right 會返回一個插入點索引 idx，表示找到的索引 idx 是第一個大於 (timestamp, chr(255)) 的位置，這樣可以有效找到 timestamp <= 給定的 timestamp 的所有符合條件的最後一個位置。**


        if idx == 0:                                                        **當 idx == 0 時，說明所有的時間戳都比給定的 timestamp 大，找不到符合條件的值，因此返回空字串 **
            return ""

        return values[idx - 1][1]                                            **values[idx - 1] 給出的是 (timestamp, value)，也就是某一個符合條件的時間戳和它的值。**
                                                                             **[1] 表示從這個元組中取出第二個元素，即 value**


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
