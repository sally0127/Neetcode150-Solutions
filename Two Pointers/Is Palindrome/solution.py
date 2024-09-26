import re

class Solution:
  
    def isPalindrome(self, s: str) -> bool:
      
        # Step 1: Filter and normalize the string
      
        filtered_string = re.sub(r'[^A-Za-z0-9]', '', s).lower()

        # Step 2: Use two pointers to check for palindrome
      
        left, right = 0, len(filtered_string) - 1

        while left < right:
          
            if filtered_string[left] != filtered_string[right]:
              
                return False
              
            left += 1
          
            right -= 1

        return True
