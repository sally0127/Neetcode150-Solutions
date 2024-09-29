**Is Palindrome**
-
🔗 Link: Is Palindrome(https://neetcode.io/problems/is-palindrome)

💡 Difficulty: Easy

🛠️ Topics:  string ,character traversal,two-pointer strategy

===========================================================================

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"
Output: true

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"
Output: false

Explanation: "tabacat" is not a palindrome.

Constraints:

．1 <= s.length <= 1000

．s is made up of only printable ASCII characters.
======================================================================================

**UMPIRE Method**:

**Understand**:

1.What are the inputs and outputs?

．The input is a string s, and the output is a boolean value indicating whether the string is a palindrome.

2.What is the definition of a palindrome?

．A palindrome is a string that reads the same forwards and backwards.

3.Should case and non-alphanumeric characters be ignored?

．Yes, case and non-alphanumeric characters should be ignored.

4.Is an empty string considered a palindrome?

．Yes, an empty string is considered a palindrome.

5.Are there any requirements on time and space complexity?

．There are no specific requirements, but we aim for efficiency.

6.Can you provide some test cases?

．"A man, a plan, a canal: Panama" should return True.

．"race a car" should return False.

．" " should return True (an empty string).

**Match**

This problem falls under the string processing category, utilizing character traversal, filtering, and the two-pointer strategy.

**Plan**
1.Create a regular expression to filter characters, keeping only alphanumeric characters and converting them to lowercase.

2.Use two pointers, one starting from the beginning of the string and the other from the end, comparing the characters at both pointers.

‧If they are the same, move the pointers inward; if not, return False.

．If the traversal is complete, return True.

3.Pseudocode

function is_palindrome(s: str) -> bool:

    filtered_string = filter non-alphanumeric characters from s and convert to lowercase
    
    left = 0
    
    right = length of filtered_string - 1
    
    while left < right:
    
        if filtered_string[left] != filtered_string[right]:
        
            return False
            
        left += 1
        
        right -= 1
        
    return True

**Implement**

see solution.py

**Review**

1.Check the implementation with test cases:

．print(is_palindrome("A man, a plan, a canal: Panama")) should output True.

．print(is_palindrome("race a car")) should output False.

．print(is_palindrome(" ")) should output True.

2.Step through the code to ensure it returns the correct results in different scenarios.

**Evaluate**

．Time Complexity: O(N), as the string is traversed twice: once for filtering and once for comparison.

．Space Complexity: O(N), due to storage of the filtered string.

**Discussion of pros and cons:**

．Pros: The code is simple and readable, effectively checking for palindromes using the two-pointer technique.

．Cons: Additional space is used to store the filtered string, which may lead to extra memory usage for large inputs.
