class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        out = 1
        pos = []
        time = []
        for i in range(n):
            pos.append((position[i], speed[i]))
        pos = sorted(pos, key= lambda x: x[0], reverse=True)
        print(pos)
        for i in range(n):
            time.append((target - pos[i][0]) / pos[i][1])
        for i in range(1, n):
            if time[i] == time[i - 1]:
                continue
            if time[i] > time[i - 1]:
                out += 1
            else:
                time[i] = time[i - 1]
        return out
        


        