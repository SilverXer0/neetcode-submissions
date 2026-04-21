class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        for i in range(len(position)):
            fleets.append((position[i], speed[i]))
        
        fleets = sorted(fleets, key = lambda x: x[0], reverse = True)
        stack = []

        for pos, spd in fleets:
            i = (target - pos) / spd
            stack.append(i)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)