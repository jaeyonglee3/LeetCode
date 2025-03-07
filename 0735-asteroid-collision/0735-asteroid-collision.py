class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            add_curr = True

            while stack and (asteroid < 0 and stack[-1] > 0) and add_curr:
                # then, we have some collisions to deal with
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    add_curr = False
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    add_curr = False
            
            if add_curr:
                stack.append(asteroid)
        
        return stack
            

