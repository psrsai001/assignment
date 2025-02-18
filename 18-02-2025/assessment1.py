class PatternMatchingSolution:
    def isMatch(self, s: str, p: str) -> bool:
        import re

        matched = re.match(rf"{p}", s)
        if not matched:
            return False
        if matched.group() == s:
            return True
        return False


class StrMultSolution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


class ContainsMostWaterSolution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        n = len(height)
        left = 0
        right = n - 1

        while left < right:
            w = right - left
            l = min(height[left], height[right])
            max_area = max(max_area, w * l)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
