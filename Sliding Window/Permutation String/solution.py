from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1) # 計算 s1 中每個字母的頻率
        window_count = Counter()  # 用於記錄當前窗口中的字母頻率

        left = 0  # 初始化窗口的左指針
        for right in range(len(s2)):
            # 增加右邊窗口的字母到 window_count
            window_count[s2[right]] +=1

            # 當窗口大小超過 s1 長度時，縮小左邊窗口
            if right - left + 1 > len(s1):
                if window_count[s2[left]] == 1:
                    del window_count[s2[left]]   # 如果字母頻率為 1，直接刪除該鍵值
                else:
                    window_count[s2[left]] -= 1  # 否則減少字母頻率
                left += 1  # 左指針右移，縮小窗口
                
            # 檢查當前窗口的字符頻率是否與 s1 的頻率相等
            if window_count == s1_count:
                return True  # 找到符合條件的子字串，返回 True
    
        return False  # 如果遍歷完 s2 沒有找到符合的子字串，返回 False
