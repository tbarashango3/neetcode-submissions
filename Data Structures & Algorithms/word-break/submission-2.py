class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        #can reuse words unlimited times
        #split s into words that appear in dict
        memo = {}
        
        def search(s):
            if s in memo:
                return memo[s]
            for word in wordDict:
                if s == word:
                    memo[s] = True
                    return True
                if s.startswith(word):
                    #print(s[len(word):])
                    if search(s[len(word):]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        
        return search(s)

        
                

        