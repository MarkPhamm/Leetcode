class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # SC: O(n)
        # TC: O(n)
        # idea
        # Step 1: create a stack data structure and loop through all the asteroids
        # Step 2: create collision: as long as there is an element in the stack, the current asteroid < 0 and the last asteroid > 0, there will be a collision 
        # * Step 2.1: if the negative asteroid win, pop the last element from the stack
        # * Step 2.2: if the positive asteroid win, change asteroid to 0 so that we won't add it to the stack
        # * step 2.3: if there's a tie, pop the last element and change asteroid to 0
        # Step 3: add to the stack if the asteroid is != 0

        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0: # creating all collision
                if abs(a) > abs(stack[-1]): # in case the negative asteroid win -> pop the last element in the stack
                    stack.pop()
                elif abs(a) < abs(stack[-1]): # in case the positive asteroid win -> don't add the negative asteroid to the stack
                    a = 0
                else: # in case the no asteroid win -> don't add the negative asteroid to the stack and pop the positive asteroid
                    stack.pop()
                    a = 0
            
            if a != 0:
                stack.append(a)        

        return stack 


        
        