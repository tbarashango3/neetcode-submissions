class Solution:
    def isPalindrome(self, s: str) -> bool:
        new1 = ''
        new2 = ''

        for char in s:
            if char.isalnum():
                new1 += char.lower()
                new2 += char.lower()
        print(list(new1))
        print(list(reversed(new2)))
        return list(new1) == list(reversed(new2))

        