**Max Water Container**
-
🔗 Link: Max Water Container(https://neetcode.io/problems/max-water-container)

💡 Difficulty: Medium

🛠️ Topics: Array, Two Pointers,Greedy Algorithm,Mathematical Optimization,Sliding Window

======================================================================================

**Understand**

．You can randomly choose two bars to form a container: Correct, you can select any two bars to create a container. The amount of water the container can store depends on the height of the two bars and the distance between them.

．The goal is to maximize the water storage: Yes, that’s the objective. The water volume is determined by the minimum height of the two bars and their horizontal distance: min(height[left], height[right]) * (right - left).

．The heights of the two bars can be the same: Correct, the two bars can have the same height, and this doesn’t affect the calculation of the water volume.

．The bar heights cannot be negative: Correct, the heights are non-negative integers, so there won’t be any negative values.

**Match**

．Two-pointer technique: You correctly mentioned the two-pointer technique, which is the optimal approach for this problem. Specifically, one pointer starts from the left (left), and the other pointer starts from the right (right), and we narrow down the range step by step.

．Pointer movement strategy: The key idea of the two-pointer method is that you move the pointer on the side of the shorter bar (if height[left] < height[right], move the left pointer rightward; otherwise, move the right pointer leftward). This gives a chance to find a taller bar, potentially increasing the water storage.

**Plan**

1.Initialize two pointers:

．The left pointer (left) points to the leftmost element in the array (0).

．The right pointer (right) points to the rightmost element in the array (n-1).

2.Calculate the water volume:

．For each pair of bars, calculate how much water they can hold:
    ．water = min(height[left], height[right]) * (right - left), where min() takes the shorter of the two bars to determine the height of the water, and (right - left) is the horizontal distance between the two bars.
    
3.Update the maximum water volume:

．After calculating the current water volume, update a variable max_water to store the current maximum water volume.

4.Move the pointers:

．Move the pointer of the shorter bar (if height[left] < height[right], move the left pointer rightward, otherwise move the right pointer leftward). This might help to find a taller bar and potentially increase the water volume.

5.Repeat until the two pointers meet:

．The loop continues until the left and right pointers meet.

**Implement**

see solytion.py

**Review**

．Edge cases:

1.Minimum case: When the array length is less than 2, the code should return 0 because you need at least two bars to form a container. In this case, we assume the input has at least two bars.

2.Same-height bars: If the two bars have the same height, just calculate their distance. The code already handles this correctly.

3.All bars are of the same or close height: The code will still move the pointers and eventually find the best result.

4.No valid container: Won’t happen, as there are always at least two bars to form a container.

**Evaluate**

．Time complexity: The algorithm moves the pointers only once, and in the worst case, each bar will only be visited once. Therefore, the time complexity is O(n).

．Space complexity: We are only using constant space to store the variables left, right, and max_water. So, the space complexity is O(1).


