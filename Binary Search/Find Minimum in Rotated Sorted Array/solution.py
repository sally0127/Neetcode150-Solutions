from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0, len(nums) - 1

        while left < right :
            mid = (left + right) // 2       

            if nums[mid] > nums[right]:
                # 最小值在右半部分
                left = mid + 1
            else:
                # 最小值在左半部分或是 mid
                right = mid
        return nums[left]   # 或者 nums[right]，因為 left == right

======================================================================

(1)from typing import List 是 Python 中用來引入 型別註解 的語法，用來指定函式參數或返回值的類型。在 LeetCode 或其他需要清楚型別的環境中，這樣的型別註解可以讓程式更具可讀性和一致性。

什麼時候需要使用？

．當題目明確指出輸入是列表時（例如 List[int]），引入 List 會讓函式的參數型別更清晰。

．在一些題目中，使用 List 是為了符合系統的要求，尤其是像 LeetCode 或其他測試平台，它們通常會有自動型別檢查。

(2)為什麼不是 right = mid - 1？

如果設置成 right = mid - 1，我們可能會略過 mid，而在這個問題中，我們希望每次迭代都確保範圍中包含潛在的最小值。因此，當我們確定最小值位於左半部分或是 mid 時，我們需要保留 mid，所以設置 right = mid。

如果是right = mid，我們也只要再迭代一次，就可以找到最小值。
