class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right =len(numbers)-1
        while left < right :
            input_nums = numbers[left] + numbers[right]

            if input_nums == target:
                return [left + 1, right + 1]
            elif input_nums < target:
                left+=1
            else :
                right-=1
