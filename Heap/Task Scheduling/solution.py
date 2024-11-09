from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 計算每個任務的頻率
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())


        # 找到具有最高頻率的任務數量
        max_freq_tasks = sum(1 for count in task_counts.values() if count == max_freq)


        # 計算最小週期數
        part_count = max_freq - 1 
        empty_slots = part_count * ( n- ( max_freq_tasks - 1))
        available_tasks = len(tasks) - max_freq * max_freq_tasks
        idles = max(0,empty_slots - available_tasks)


        return len(tasks) + idles
