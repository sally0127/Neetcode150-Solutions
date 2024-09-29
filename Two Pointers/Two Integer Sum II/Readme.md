**Two Integer Sum II**
-
🔗 Link: Two Integer Sum II(https://neetcode.io/problems/two-integer-sum-ii)

💡 Difficulty: Medium

🛠️ Topics: Array,Two Pointers

==============================================================================

Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3
Output: [1,2]

Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1, index2 = 2. We return [1, 2].

Constraints:

．2 <= numbers.length <= 1000

．-1000 <= numbers[i] <= 1000

．-1000 <= target <= 1000

**UMPIRE Method**:

**Understand**

．The index starts from 1.

．There is only one valid solution.

．Index1 must be less than Index2.

**Match**:

．We can use two pointers: one pointing to the left (low pointer) and the other to the right (high pointer).

．When the sum of the two numbers equals the target, we have found the solution.

．If the sum is less than the target, move the low pointer forward to increase the sum.

．If the sum is greater than the target, move the high pointer backward to decrease the sum.

．Repeat this process until the solution is found.

**Plan**:

．First, set up the left and right pointers, where the left pointer starts from index 0 and the right pointer starts from the last index (n-1).

．Keep searching until the sum of the two numbers is found.

．If the sum equals the target, return [left + 1, right + 1] (since the index is 1-based).

．If the sum is less than the target, move the left pointer to the right by one to increase the sum.

．If the sum is greater than the target, move the right pointer to the left by one to decrease the sum.

**Implement**:

see solution.py

**Review**:

In this step, we need to check the code for any logical errors or edge cases. For example:

．Can it handle the minimum case (such as an array with only two elements)?

．When all elements are the same or close to each other, can it still find the correct solution?

Based on our previous analysis, these edge cases should be well handled.

**Evaluate**:

Evaluate the time and space complexity of the code:

．The time complexity is O(n) because we use the two-pointer method, which traverses the array at most once.

．The space complexity is O(1) because we only use a fixed amount of extra space to store the left and right pointers.
