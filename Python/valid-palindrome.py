class Solution:
    def isPalindrome(self, s: str) -> bool:
        AlphaNumeric = ""
        letters = "qertyuiopasdfghjklzxcvbnm1234567890"
        for c in s.lower():
            if c in letters:
                AlphaNumeric += c
        return AlphaNumeric == AlphaNumeric[::-1]