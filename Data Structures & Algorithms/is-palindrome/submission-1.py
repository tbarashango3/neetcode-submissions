class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(letter.lower() for letter in s if letter.isalnum())
        rev = ""
        for i in range(len(s) - 1, -1, -1):
            rev += s[i]
        return rev == s



        