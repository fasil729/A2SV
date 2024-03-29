class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
 
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(key=lambda x: (x[0], x[1]), reverse=True) # desc order : closer to traget comes first
        stack = []
        for x, v in cars:
            dist = target - x # remaning distance to tagret
            if not stack:
                stack.append(dist/v) # arrivalTime = dist/v
            elif dist/v > stack[-1]: # car arrives late -> thus does not join previous fleet and forms its own fleet
                stack.append(dist/v)
            # if curr arrivalTime is <= prev arrivalTime -> then curr car joins prev fleet and gets discolved into it (aka we don't need to do anything)
        return len(stack)
