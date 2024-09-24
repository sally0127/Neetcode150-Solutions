class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        # Step 1: Compute left products
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        # Step 2: Compute right products and multiply with left
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        return output
