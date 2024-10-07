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
