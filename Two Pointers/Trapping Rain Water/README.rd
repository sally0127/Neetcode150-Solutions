**Trapping Rain Water**
-
🔗 Link: Trapping Rain Water(https://neetcode.io/problems/trapping-rain-water)

💡 Difficulty: Hard

🛠️ Topics: Array, Hashmap

=========================================================================

You are given an array non-negative integers heights which represent an elevation map. Each value heights[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9

Constraints:

．1 <= height.length <= 1000

．0 <= height[i] <= 1000

=============================================================================

**Understand**

1.Heights cannot be negative: Each bar in the array has a non-negative height (0 or positive integers), and each bar has a width of 1. The amount of water that can be trapped depends on the heights of the bars and the space between them.

2.Calculating the maximum value: The goal is to calculate the maximum volume of water that can be trapped between the bars.

3.Random heights: The heights of the bars can be any non-negative integer, meaning the data is random.

4.The figure is an elevation map: The problem can be visualized as an elevation map where each bar represents the terrain's height, and the amount of water depends on the height differences between the bars.

**Match**

1.Using two-pointer technique: You can use two pointers to find the areas where water can be trapped.

2.Shrinking the range using two-pointer technique: This is the key approach for solving the problem. By moving the pointers from the left and right ends of the array towards the center, you can calculate the water trapped and adjust the range accordingly.

**Plan**

1.Initialize two pointers:

Left pointer (left) starts at the leftmost position of the array (0).

Right pointer (right) starts at the rightmost position of the array (n-1).

2.Calculate the trapped water:

For each bar, calculate the water that can be trapped between the bars:

Water = min(left_max, right_max) * (right - left), where left_max and right_max are the highest bars on the left and right sides, respectively.

3.Update the maximum water:

After calculating the water for the current step, update a variable max_water to store the maximum amount of water found so far.

4.Move the pointers:

Move the pointer corresponding to the smaller bar height, as this is the only way to potentially increase the trapped water.

5.Repeat until the two pointers meet:

The loop stops when left and right pointers meet.

**Implement**

see solution.py

**Review**

In this step, let’s verify the edge cases and special scenarios:

．Minimum case: If the array has fewer than two bars, the function should return 0, as at least two bars are needed to trap water.

．Bars of the same height: If two bars have the same height, we simply calculate the water between them based on their distance, and the code already handles this correctly.

．All bars have the same or similar height: The code will still correctly compute the trapped water in such cases.

**Evaluate**

．Time complexity: O(n), as each bar is visited only once.

．Space complexity: O(1), as only a constant amount of space is used to store variables.





