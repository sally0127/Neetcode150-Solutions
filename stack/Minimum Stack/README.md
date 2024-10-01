**Minimum Stack**
-
🔗 Link:Minimum Stack(https://neetcode.io/problems/minimum-stack)

💡 Difficulty: Medium

🛠️ Topics: Push,Pop,Top,Get Minimum

===================================================================

Design a stack class that supports the push, pop, top, and getMin operations.

．MinStack() initializes the stack object.

．void push(int val) pushes the element val onto the stack.

．void pop() removes the element on the top of the stack.

．int top() gets the top element of the stack.

．int getMin() retrieves the minimum element in the stack.

Each function should run in O(1) time.

Example 1:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:

MinStack minStack = new MinStack();

minStack.push(1);

minStack.push(2);

minStack.push(0);

minStack.getMin(); // return 0

minStack.pop();

minStack.top();    // return 2

minStack.getMin(); // return 1

Constraints:

．-2^31 <= val <= 2^31 - 1.

．pop, top and getMin will always be called on non-empty stacks.

===========================================================================

**Understand**

You need to design a stack class, MinStack, which not only supports basic operations (push, pop, top) but also includes an additional feature: quickly querying the minimum value in the stack. Each operation must have a time complexity of O(1), meaning all operations should complete in constant time, regardless of the size of the stack.

Specific Requirements:

  ．push(val): Push the element val onto the stack.
  
  ．pop(): Remove the element on the top of the stack.
  
  ．top(): Get the top element of the stack.
  
  ．getMin(): Quickly return the minimum element in the stack.

**Match**

For problems requiring constant-time retrieval of the minimum value, a common solution is to use two stacks:

1.Main Stack (stack): Stores all elements.

2.Minimum Value Stack (min_stack): Whenever a new element is inserted via the push operation, it records the current minimum value. Thus, we can query the current minimum value in O(1) time by checking the top element of the minimum value stack.

**Plan**

1.Initialization: Define two stacks: stack and min_stack.

2.push(val): Push the element onto stack, and check if the new element is smaller than or equal to the top element of min_stack. If so, also push it onto min_stack.

3.pop(): Remove the top element from stack, and check if this element is equal to the top of min_stack. If so, pop it from min_stack as well.

4.top(): Directly return the top element of stack.

5.getMin(): Return the top element of min_stack, as this is always the current minimum value.

**Implement**

see solution.py

**Review**

1.Edge Cases:

．If the stack is empty, getMin() and top() methods should not be called, as these are illegal operations. It can be assumed that when these methods are called, there is at least one element in the stack.

．The push and pop operations need to synchronize the maintenance of min_stack, ensuring that whenever an element is popped or pushed, the minimum value stack remains consistent.

2.Testing:

．Insert and remove some positive and negative numbers, checking if the minimum value is updated correctly.

．Test the scenario where there is only one element to ensure getMin() works properly.

**Evaluate**

．Time Complexity: All operations (push, pop, top, getMin) are O(1).

．Space Complexity: Additional space is used to store the minimum value stack, which in the worst case could be as long as the main stack, leading to a space complexity of O(n).
