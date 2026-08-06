class Solution:
    def isValid(self, s: str) -> bool:
        m = {}
        m[')'] = '('
        m[']'] = '['
        m['}'] = '{'
        opening = []
        if len(s) % 2 == 1:
            return False
        for char in s:
            if char in ['(', '[', '{']:
                opening.append(char)
            elif len(opening) > 0 and m[char] == opening[-1]:
                opening.pop()
            else:
                return False
        if not opening:
            return True
        return False
        
        
        
        