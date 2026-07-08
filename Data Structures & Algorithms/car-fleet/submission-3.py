class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = []
        for i in range(len(position)):
            fleets.append((position[i], speed[i]))

        fleets = sorted(fleets, key = lambda x: x[0])

        stack = []
        for pos, spd in fleets:
            time = (target - pos) / spd
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack)
