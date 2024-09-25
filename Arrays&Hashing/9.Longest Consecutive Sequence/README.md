**9.Longest Consecutive Sequence**
-
🔗 Link: Longest Consecutive Sequence(https://neetcode.io/problems/longest-consecutive-sequence)

💡 Difficulty: Medium

🛠️ Topics: Array, Hashset

====================================================================================
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4

Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

Constraints:

．0 <= nums.length <= 1000

．-10^9 <= nums[i] <= 10^9

======================================================================================================

**UMPIRE Method:**

**Understand**

1.Key Questions:

．What is a consecutive sequence? Two numbers are consecutive if their difference is 1 (e.g., 1, 2, 3, 4).

．Can the elements in the array be negative? — Yes, the numbers can be positive, negative, or zero.

．Are duplicates allowed in the array? — The problem doesn’t explicitly forbid duplicates, so we need to handle that.

2.Key Issue:

．How do we determine the starting number of a sequence? If a number has no preceding number (i.e., num - 1 doesn't exist), then it is the starting point of a sequence.

．How can we ensure the time complexity is O(n)? By using a HashSet to store and search for numbers, as looking up numbers in a set takes O(1) time.

**Match**

1.Data structure: We can use a Hash Set to store all the numbers in the array. Hash Sets remove duplicates and allow for fast lookups (O(1)).

2.Algorithm idea: We can iterate over each number, check if it’s the start of a sequence, and then calculate the length of that sequence.

**Plan**

1.Store the data: First, put all the numbers in a set to remove duplicates and make lookups efficient.

2.Identify sequence start: If num - 1 isn’t in the set, it means num is the start of a sequence.

3.Calculate sequence length: Starting from the identified sequence start, check if num + 1, num + 2, etc., are in the set, and count the length of the sequence.

4.Update the maximum length: If a longer sequence is found, update the longest length.

**Implement**

see solution.py

**Review**

1.Correctness: Consider edge cases like an empty array, an array with all duplicate elements, or an array containing negative numbers.

2.Time Complexity: Since each number is visited at most once, the time complexity is O(n).

3.Space Complexity: We used an additional set to store the numbers, so the space complexity is O(n).

**Evaluate**

Edge Cases:

．If the array is empty, return 0.

．If all numbers in the array are non-consecutive, return 1.

．If the entire array forms a consecutive sequence (e.g., [1, 2, 3, 4]), return the length of the entire array.
