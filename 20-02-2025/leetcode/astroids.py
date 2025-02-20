class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for astroid in asteroids:
            if astroid > 0:
                ans.append(astroid)
            elif len(ans) == 0:
                ans.append(astroid)
            else:
                while len(ans) and ans[-1] > 0 and ans[-1] < -astroid:
                    ans.pop()
                if len(ans) == 0:
                    ans.append(astroid)
                elif ans[-1] == -astroid:
                    ans.pop()
                elif ans[-1] < 0:
                    ans.append(astroid)

        return ans
