class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for asteroid in asteroids:
            flag = True
            while result and result[-1] > 0 > asteroid:
                if result[-1] < abs(asteroid):
                    result.pop(-1)
                    continue
                elif result[-1] == abs(asteroid):
                    result.pop(-1)
                flag = 0
                break
            if flag:
                result.append(asteroid)
        return result
