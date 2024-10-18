class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: 使用快慢指針檢測循環
        slow = nums[0]
        fast = nums[0]

        # 快慢指針第一次相遇
        while True :
            slow = nums [slow]
            fast = nums [nums[fast]]
            if slow == fast:
                break

        # Step 2: 找到循環的起點（即重複的數字）
        slow = nums[0]
        while slow != fast :
            slow = nums [slow]
            fast = nums [fast]

        return slow  # 返回重複的數字
