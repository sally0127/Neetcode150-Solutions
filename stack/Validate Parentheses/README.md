**Validate Parentheses**
-
🔗 Link: Validate Parentheses(https://neetcode.io/problems/validate-parentheses)

💡 Difficulty: Easy

🛠️ Topics: 

=============================================================================

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    1.Every open bracket is closed by the same type of close bracket.
    
    2.Open brackets are closed in the correct order.
    
    3.Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"
Output: true

Example 2:

Input: s = "([{}])"
Output: true

Example 3:

Input: s = "[(])"
Output: false

Explanation: The brackets are not closed in the correct order.

Constraints:

．1 <= s.length <= 1000

**Understand**

1.Every opening bracket must have a corresponding closing bracket: Each opening bracket (, {, [ must have a matching closing bracket ), }, ].

2.Brackets must be closed in the correct order: For example, if an opening bracket ( appears before {, you cannot close it with } or ), they must close in the reverse order.

3.The string may contain different types of brackets: The string may include multiple types of brackets, and their matching rules are independent.

4.Every closing bracket must have a corresponding opening bracket: There cannot be any extra closing brackets, nor should there be any unmatched opening brackets.

**Match**

A common solution to this problem is to use a stack data structure, which helps to efficiently track the open and close brackets and ensure they match in the correct order.

Here is the thought process:

．Use a stack to store opening brackets, and when encountering a closing bracket, pop the corresponding opening bracket from the stack to check if they match.

．If the closing bracket does not match the top of the stack, the string is invalid.

．Finally, once all characters are processed, the stack should be empty to ensure all brackets are matched.

**Plan**

1.Initialize an empty stack: This will store the opening brackets.

2.Traverse through the string: If it's an opening bracket, push it onto the stack; if it's a closing bracket, check whether it matches the last opening bracket in the stack.

3.Check for mismatches: If at any point a closing bracket cannot be matched (stack is empty or brackets don't match), return false.

4.Final check: Once all characters are processed, if the stack is not empty, it means there are unmatched opening brackets, return false. Otherwise, return true.

**Implement**

see solution.py

**Review**

．Edge cases:
    ．If the string is empty "", return true because there are no brackets to match.
    
    ．Single bracket cases like "(" or ")" should return false since there is no pair to match.
    
    ．Complex cases with multiple types of brackets, such as "{[()]}", should be correctly matched.

**Evaluate**

．Time complexity: The time complexity is O(n), where n is the length of the string since each character is processed once.

．Space complexity: The space complexity is O(n) because, in the worst-case scenario, the stack will store all the opening brackets.


