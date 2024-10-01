from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # 遍歷整個 tokens
        for token in tokens:
            if token in "+-*/":  # 如果 token 是運算符
                # 確保堆疊中有至少兩個運算數
                if len(stack) < 2:
                    raise ValueError("Not enough operands in stack for operation")

                # 先 pop 出兩個運算數
                num2 = stack.pop()
                num1 = stack.pop()

                # 根據運算符進行對應的計算
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num1 - num2
                elif token == "*":
                    result = num1 * num2
                elif token == "/":
                    # 向零截斷
                    result = int(num1 / num2) if num1 * num2 >= 0 else -(-num1 // num2)

                # 將計算結果推回堆疊
                stack.append(result)
            else:
                # 如果 token 是數字，轉換為整數並放入堆疊
                stack.append(int(token))

        # 最後堆疊中的唯一值就是結果
        if len(stack) != 1:
            raise ValueError("The expression did not evaluate to a single result.")
        
        return stack.pop()
