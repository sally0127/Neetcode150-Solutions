from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums) - 1

        while left <= right :
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            #判斷左半部分是否排序
            if nums[left] <= nums[mid]:
                # 判斷 target 是否在左半部分
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # 否則右半部分排序
            else:
                # 判斷 target 是否在右半部分
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return - 1

  ==============================================================

**過程中犯的錯**

在提交過程中出現錯誤，結果是邊界情況出錯。犯錯如下:

while 的條件應該是 left <= right 而不是 left < right。這樣可以保證當 left 和 right 相等時也能檢查該位置的元素。

測試建議：

確保測試用例包括以下情況：

．數組為空。

．數組僅包含一個元素。

．數組旋轉的情況。

．目標值在數組的開始和結束部分。

．目標值不在數組中的情況。

這樣可以保證你的程式碼在各種「邊界情況」下都能正確運行。希望這能幫助你成功提交！如果還有其他問題，隨時告訴我。

**邊界情況**

邊界情況（boundary cases）指的是在程序或算法中處理極端或特定輸入情況的情況，這些情況可能會導致錯誤或不預期的行為。這些情況通常包括：

1.空輸入：例如，在查找元素的情況下，如果數組為空，算法應該如何處理。

2.單個元素：如果數組中只有一個元素，算法是否能正確返回該元素的索引或 -1。

3.重複邊界：在使用指標（如 left 和 right）時，當它們相等時應如何處理。

4.極大或極小的數據：例如，數組包含非常大的數字或非常小的數字時，算法的表現是否正常。

5.範圍邊界：例如，數組的第一個或最後一個元素是目標元素的情況。

6.全部元素相同：例如，數組中的所有元素都是相同的，且這個值就是目標。

在你的搜索算法(這題)中，邊界情況的例子可能包括：

．當 nums 為空數組時，應返回 -1。

．當 nums 僅包含一個元素時，應檢查該元素是否為目標。

．當 left 和 right 相等時，仍然需要檢查該索引的元素是否為目標。

處理這些邊界情況有助於確保算法的穩定性和正確性。




