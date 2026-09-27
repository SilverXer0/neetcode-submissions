class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = sorted(cars, key = lambda x: x[0], reverse = True)

        for pos, speed in cars:
            time = (target - pos) / speed
            if stack and time > stack[-1]:
                stack.append(time)
            elif not stack:
                stack.append(time)

        return len(stack)

