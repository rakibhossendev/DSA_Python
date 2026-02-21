class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = "".join(ch.lower() for ch in s if ch.isalnum())
        isPalindrome = True
        left = 0
        right = len(clean_str) - 1
        while True:
            if left >= right:
                break
            if clean_str[left] != clean_str[right]:
                isPalindrome = False
            left += 1
            right -= 1
        return isPalindrome 
