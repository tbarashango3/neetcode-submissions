class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products = sorted(products)
        for i in range(len(searchWord)):
            ans.append([])
            w = searchWord[0:i+1]
            for prod in products:
                if prod.startswith(w):
                    print(w)
                    ans[i].append(prod)
            #ans[i] = sorted(ans[i])
            if len(ans[i]) > 3:
                ans[i] = ans[i][0:3]
        return ans



