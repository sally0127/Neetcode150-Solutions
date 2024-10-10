from collections import Counter,defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t) # 計算 t 中每個字符的頻率
        required = len(dict_t) # 需要匹配的不同字符數量
        left,right = 0,0  # 初始化指針
        formed = 0 # 當前窗口中已經匹配的字符數量
        window_counts = defaultdict(int)   # 窗口中字符的頻率

        # 儲存最小窗口的信息
        min_len = float("inf")
        min_left,min_right = 0,0

        while right < len(s):
            character = s[right]  # 擴展窗口，將右指針指向的字符加入窗口
            window_counts[character] +=1


            # 檢查當前字符是否滿足 t 中的需求
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1   # 如果滿足，增加已匹配的字符數量

            # 嘗試縮小窗口，直到不滿足條件為止
            while  formed == required:
                character = s[left] # 縮小窗口，將左指針指向的字符移除

                # 更新最小窗口的長度和位置
                if right -left + 1 < min_len:
                    min_len = right - left + 1
                    min_left,min_right = left, right + 1  # +1 是因為右指針是獨佔的

                window_counts[character] -= 1  # 移除字符，更新頻率
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1  # 如果字符不再滿足要求，減少已匹配的字符數量

                left += 1 # 移動左指針，縮小窗口
            
            right += 1  # 移動右指針，擴展窗口

        return "" if min_len == float("inf") else s[min_left:min_right]  # 返回最小窗口
