class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleet = ((speed[i], position[i]) for i in range(len(position)))

        fleet = sorted(fleet, key = lambda x: x[1])
        for s, p in fleet:
            time = (target - p) / s
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack)