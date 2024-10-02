class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        # 回溯函數，當前的組合、左括號和右括號的數量
        def backtrack(current_str,open_count,close_count):
            # 如果左右括號都已經用完了，加入結果集
            if open_count == n and close_count == n:
                result.append(current_str)
                return


            # 如果左括號還可以放
            if open_count < n :
                backtrack(current_str + '(',open_count + 1,close_count)

            # 如果右括號可以放（前提是已有的左括號比右括號多）
            if close_count < open_count :
                backtrack(current_str + ')',open_count ,close_count + 1)
        
        #初始條件
        backtrack("",0,0)
        return result
