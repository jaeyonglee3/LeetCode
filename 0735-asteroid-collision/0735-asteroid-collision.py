class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # paraphrase:
        # want to know the result after collisions have processed
        # the position of the asteroid in the array represents its posiiton in space
        
        # collision rules if A and B collide:
            # abs(A) > abs(B), B is destroyed
            # abs(A) == abs(B), both are destroyed
        
        # dry runs:
        # input: [10, 2, -5]
        # stack: 10

        # input: [1, 2, 3]
        # output: [1, 2, 3]
        # edge case: all asteroids are going in same direction will never collide

        # input: []
        # output: []

        # input: [10, 10, -10, 5]
        # stack: -10

        # input: [-10, 7, 5]
        # output: [-10, 7, 5]
        # no collisions because index represents position, 7, 5 go right and -10 goes left
        # intuition: the only case collision occurs between items at i, j where j > i is 
        # if asteroid at j is negative and asteroid at i is positive

        # approach:
        # go through each asteroid from left to right and maintain a stack
        # deal with collisions so the stack always shows the state after collisions
        # the stack will contain the result

        stack = []

        for ast in asteroids:
            ast_destroyed = False

            while stack and not ast_destroyed and stack[-1] > 0 and ast < 0:
                # a collision will occur
                if abs(ast) > abs(stack[-1]):
                    stack.pop()
                elif abs(ast) == abs(stack[-1]):
                    stack.pop()
                    ast_destroyed = True
                else:
                    # abs(ast) < abs(stack[-1])
                    ast_destroyed = True

            if not ast_destroyed:
                stack.append(ast)
        
        return stack