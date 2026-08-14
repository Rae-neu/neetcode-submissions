class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        stack = []
        res = 0

        for car in cars:
            fleet_time = (target - car[0]) / car[1]
            if len(stack) != 0 and fleet_time <= stack[-1]:
                continue
            stack.append(fleet_time)
            res += 1
        return res
