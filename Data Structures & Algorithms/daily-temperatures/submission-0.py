class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        n = len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                print("check: ", stack)
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
                print(res)
            stack.append((t, i))
            print("append: ", stack)
        return res


                
            


        

        