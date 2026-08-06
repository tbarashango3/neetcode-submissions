class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        #print("sentences: ", sentences)
        #print("times ", times)
        self.sentences = sentences
        self.times = times
        self.w = ""

    def input(self, c: str) -> List[str]:
        print(self.times)
        if c == "#":
            for i in range(len(self.sentences)):
                if self.w == self.sentences[i]:
                    self.times[i] += 1
                    self.match = True
                    break
            if not self.match:
                self.sentences.append(self.w)
                self.times.append(1)
            self.w = ""
            return []
        self.o = []
        print("c", c)
        self.w += c
        self.match = False
        for i in range (len(self.sentences)):
            #print("word: ", self.w)
            #print("substring: ", self.sentences[i][0: len(self.w)])
            if self.w == self.sentences[i][0: len(self.w)]:
                self.o.append((self.sentences[i], self.times[i]))
                self.match = True

        #print("output: ", self.o)
        self.o.sort(key=lambda x: (-x[1], x[0]))
        return [x[0] for x in self.o[:3]]
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
