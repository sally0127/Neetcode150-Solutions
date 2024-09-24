**7.Products of Array Discluding Self**
-----------------------------------------------
🔗 [Link: Products of Array Discluding Self ](https://neetcode.io/problems/products-of-array-discluding-self)
💡 Difficulty: Medium
🛠️ Topics: Array, Hashing

============================================================================
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
． 2 <= nums.length <= 1000
． -20 <= nums[i] <= 20

=====================================================================

**UMPIRE Method:**

**Uderstand**
．Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
．Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
．Verify that you and the interviewer are aligned on the expected inputs and outputs.
1.Can the nums array be empty?
2.Are there any negative numbers or 0 in the array?
3.Can there be duplicate elements?
4.Should we consider the case where the array length is 1?

**Match**
．See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1.Category: Array Problem
2.Related Patterns: Product, Prefix and Suffix Operations
3.Cannot use division, so the method of directly calculating the total product and then dividing by nums[i] cannot be used to solve the problem.We can use the left and right product approach, breaking the problem down into multiple traversals.

**Plan**
．Sketch visualizations and write pseudocode
．Walk through a high level implementation with an existing diagram
We can calculate it in two steps:
    1.Left Product: For each position i, calculate the product of all elements to the left of nums[i].
    2.Right Product: For each position i, calculate the product of all elements to the right of nums[i].
The final result is obtained by multiplying the left product and right product to get the result for each position.

**Implement**
．Implement the solution (make sure to know what level of detail the interviewer wants)

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

**Review**
．Re-check that your algorithm solves the problem by running through important examples
．Go through it as if you are debugging it, assuming there is a bug

**Evaluate**
．Time Complexity: O(n), because we only traverse the array twice.
．Space Complexity: O(1), although we use the output array, the additional space excluding the output part is O(1).







