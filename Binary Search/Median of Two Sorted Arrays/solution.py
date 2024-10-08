class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保證 nums1 是較短的數組，這樣我們只需在較小數組上做二分搜尋
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        # 搜尋的範圍在 nums1 數組上
        left, right = 0, m
        half_len = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2   # nums1 的切割位置
            j = half_len - i          # nums2 的切割位置

            # 調整二分搜尋的範圍
            if i < m and nums2[j - 1] > nums1[i]:
                left = i + 1   # i 太小了，必須右移
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1  # i 太大了，必須左移
            else:
                # 找到合適的 i, j，確保左半部分的最大值和右半部分的最小值
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])

                # 如果總數為奇數，中位數就是左半部分的最大值
                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                # 總數為偶數，中位數為左半部分的最大值和右半部分的最小值的平均
                return (max_of_left + min_of_right) / 2
