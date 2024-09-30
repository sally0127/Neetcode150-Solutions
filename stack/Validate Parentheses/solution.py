class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(','}':'{',']':'['}

        for char in s :
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                #如果不匹配，則返回false
                if mapping[char] != top_element:
                    return False

            else:
                stack.append(char)

        # 最終堆疊應該是空的
        return not stack
