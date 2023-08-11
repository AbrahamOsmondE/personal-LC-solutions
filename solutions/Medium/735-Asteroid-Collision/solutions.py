class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if stack == []:
                stack.append(i)
            else:
                if stack[-1] > 0 and i < 0:
                    while stack and stack[-1] > 0 and i < 0:
                        if abs(i) > abs(stack[-1]):
                            stack.pop()
                        elif abs(stack[-1]) > abs(i):
                            i = 0
                        else:
                            stack.pop()
                            i = 0
                    if i !=0:
                            stack.append(i)
                else:
                    stack.append(i)
        return stack