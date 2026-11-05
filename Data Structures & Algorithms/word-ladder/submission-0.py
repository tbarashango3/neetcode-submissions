class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        queue = deque()
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        count = 1

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return count
                for word in wordList:
                    if word not in visited:
                        #print(curr)
                        print(word)
                        diff = 0
                        for i in range(n):
                            if curr[i] != word[i]:
                                diff += 1
                        if diff ==  1:
                            queue.append(word)
                            visited.add(word)
            count += 1
        
        return 0



        