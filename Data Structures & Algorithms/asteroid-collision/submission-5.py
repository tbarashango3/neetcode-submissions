class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 2 astroids moving in sma edirection never meet
        # smaller astroid explodes, if both same size then both explode
        # loop until no more collisions happen

        collision = True
        while(collision):
            collision = False
            if len(asteroids) == 1:
                return asteroids
            i = 0
            while i < len(asteroids) - 1:
                #print(len(asteroids))
                #print(asteroids)
                #print(i)
                if asteroids[i] > 0 and asteroids[i+1] < 0:
                    collision = True
                    if asteroids[i] > abs(asteroids[i+1]):
                        del asteroids[i+1]
                    elif asteroids[i] < abs(asteroids[i+1]):
                        del asteroids[i]
                    else:
                        del asteroids[i+1]
                        del asteroids[i]
                    #continue
                i += 1
        return asteroids
            

   



        