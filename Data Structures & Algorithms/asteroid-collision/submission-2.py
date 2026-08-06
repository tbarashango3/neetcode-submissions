class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # s = []
        # for a in asteroids:
        #     s.append(a)
        changed = True
        while changed:
            i = 0
            changed = False
            while i < len(asteroids) - 1:
                # print("index: ", i)
                if asteroids[i] > 0 and asteroids[i+1] < 0:
                    changed = True
                    if asteroids[i] + asteroids[i+1] == 0:
                        asteroids.pop(i)
                        asteroids.pop(i)
                        # print(asteroids)
                    elif abs(asteroids[i]) > abs(asteroids[i+1]):
                        asteroids.pop(i + 1)
                        # print(asteroids)
                    else:
                        asteroids.pop(i)
                        # print(asteroids)
                else:
                    i += 1
        return asteroids