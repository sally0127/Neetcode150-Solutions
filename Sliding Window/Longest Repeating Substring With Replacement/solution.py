from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_count = 0
        char_count = defaultdict(int)

        for right in range(len(s)):
            # 增加右指針所指字符的計數
            char_count[s[right]]+=1
            max_count = max(max_count, char_count[s[right]])

            # 檢查窗口大小是否有效
            while (right - left + 1) - max_count > k:
                char_count[s[left]] -=1   #先縮小才能再往右移
                left+=1

            # 更新最大子串長度
            max_length = max(max_length, right - left + 1)

        return max_length
