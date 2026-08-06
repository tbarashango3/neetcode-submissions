class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        words = []
        temp = ""
        for i in range(len(s)):
            if s[i] != " ":
                temp += s[i]
                if i == len(s) - 1:
                    words.append(temp)
            else:
                words.append(temp)
                temp = ""
        words.reverse()
        rev = []
        spaces = len(words) - 1
        for i in range(spaces):
            words[i] += " "

        for word in words:
            for letter in word:
                rev.append(letter)
        s[:] = rev
        print(s)

        