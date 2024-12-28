class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # sign represents direction, absolute value represents size, speed is constant
        # after collision, smaller one explodes. if same size, both explode
        # two asteroids moving in the same direction never meet

        stack = []

        for asteroid in asteroids:
            should_add = True

            while stack and should_add and ((stack[-1] > 0 and asteroid < 0)):
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    should_add = False
                    stack.pop()
                else:
                    should_add = False
            
            if should_add:
                stack.append(asteroid)
        
        return stack
