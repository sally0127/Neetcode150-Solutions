class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])  # m 是行數，n 是列數
        left, right = 0, m * n - 1  # 將矩陣視為長度為 m * n 的一維數組
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]  # 找到 mid 在 2D 矩陣中的對應位置
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

  ==================================================================================

**程式碼解說**

(1)檢查特殊情況

if not matrix or not matrix[0]:
    return False

這一段代碼的作用是檢查是否給定了空的矩陣。如果 matrix 是空的（即沒有任何行），或者矩陣的第一行是空的，則直接返回 False，因為不可能在空矩陣中找到任何目標數字。

(2)矩陣的行數和列數

m, n = len(matrix), len(matrix[0])

這裡我們取得了矩陣的行數 m 和列數 n：

．m = len(matrix) 是矩陣的行數。

．n = len(matrix[0]) 是矩陣的列數。

補充:

    ．matrix 是一个二维数组（矩阵），由多行（rows）和多列（columns）组成。
    
    ．matrix[0] 表示矩阵的第一行，这个元素本身也是一个列表，包含了该行的所有列。
    
    ．len(matrix) 给出了矩阵的行数，因为它返回的是矩阵包含多少个列表（行）。
    
    ．len(matrix[0]) 则给出了第一行的列数，因为它返回的是第一行这个列表的长度，即这一行有多少个元素（列）。
    
    ．也就是說，第一步先透過matrix[0]得到矩陣第一行，之後再透過len(matrix[0])得到矩陣的列數

(3)初始化二分搜尋範圍

left, right = 0, m * n - 1

將整個 2D 矩陣視為一個 1D 排序數組，索引的範圍是從 0 到 m * n - 1，表示矩陣中所有元素的線性展開位置。例如，如果矩陣有 3 行 4 列，則矩陣展開後的索引範圍為 0 到 11。

(4)二分搜尋過程

while left <= right:
  
    mid = (left + right) // 2
  
    mid_value = matrix[mid // n][mid % n]

這裡進行二分搜尋的核心步驟：

．mid = (left + right) // 2：計算當前範圍內的中點索引 mid。

．mid // n：這是計算對應的行號。由於每行有 n 個元素，因此將 mid 除以 n 得到它對應的行。

．mid % n：這是計算對應的列號。mid 對 n 取餘數得到它在該行中的位置。

．mid_value = matrix[mid // n][mid % n]：找到這個索引對應的值，也就是矩陣中的 mid_value。

補充:

    ．因為矩陣是行在前，列在後的順序，所以不能隨意調換除法和取餘數。
    
      1.mid // n 確定的是行數，因為每行有 n 個元素，對行進行整除可以找到這個索引所在的行。
    
      2.mid % n 確定的是列數，因為對 n 取餘數可以得到這個索引在那一行中的具體位置。
    
      3.如果把它們調換，會造成行列計算錯誤，導致尋找的索引位置也不正確。

(5)比較 target 和 mid_value

if mid_value == target:
  
    return True
  
elif mid_value < target:
  
    left = mid + 1
  
else:
  
    right = mid - 1

．如果 mid_value 等於 target，說明我們已經找到了目標數字，立即返回 True。

．如果 mid_value 小於 target，說明目標數字位於右半部分，因此我們將 left 設置為 mid + 1 繼續搜尋右邊。

．如果 mid_value 大於 target，說明目標數字在左半部分，因此將 right 設置為 mid - 1。

(6)搜索失敗

return False

如果整個搜索結束後沒有找到目標數字，則返回 False。

(7)總結

這個程式碼的工作流程如下：

  1.將矩陣視為 1D 排序數組，利用二分搜尋法來進行高效搜索。
  
  2.每次搜尋時，通過計算 mid 的索引來將其轉換成對應的矩陣行和列。
  
  3.根據 mid_value 和目標值的比較結果，縮小搜尋範圍，最終找到目標或者確認目標不存在。

這樣的解法時間複雜度為 O(log(m * n))，符合題目要求。
