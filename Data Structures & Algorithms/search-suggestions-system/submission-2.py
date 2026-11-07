class Trie:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.word = True

    def startsWith(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
    
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word
            

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #self.root = Trie()
        #for p in products:
            #self.root.addWord(p)
        ans = []
        for i in range(len(searchWord)):
            ans.append([])
            w = searchWord[0:i+1]
            #if not root.startsWith(w):
                #continue
            for prod in products:
                if prod.startswith(w):
                    print(w)
                    ans[i].append(prod)
            ans[i] = sorted(ans[i])
            if len(ans[i]) > 3:
                ans[i] = ans[i][0:3]
                    
        
        return ans



