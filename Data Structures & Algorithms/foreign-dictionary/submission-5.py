class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        n = len(words)
        #print(words[2][1])
        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = []
        for i in range(n - 1):
            count = 0
            j = i+1
            if len(words[i]) > len(words[j]) and words[i].startswith(words[j]):
                return ""
            for k in range(min(len(words[i]), len(words[j]))):
                #print(words[i])
                if words[i][k] != words[j][k]:
                    adj[words[i][k]].append(words[j][k])
                    break

        print(adj)
        
        def dfs(l):
            
            if l in visited:
                return False
            if l in completed:
                return True
            visited.add(l)
            for v in adj[l]:
                if not dfs(v):
                    return False
            
            visited.remove(l)
            completed.add(l)
            w.append(l)
            return True

        visited = set()
        completed = set()
        w = []
        for char in adj:
            if not dfs(char):
                return ""
        return "".join(reversed(w))



        
            
        