class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, a in enumerate(temperatures):
            while stack and a > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((a, i))

        return res