class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for pos, spe in cars:
            time = (target - pos) / spe

            if not stack:
                stack.append(time)

            elif time <= stack[-1]:
                continue
                
            else:
                stack.append(time)
            
        return len(stack)
        
        