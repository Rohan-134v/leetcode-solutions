class Solution:
    def removeStars(self, s: str) -> str:
        stack_a = []
        for char in s:
            if char != "*":
                stack_a.append(char)
            else:
                stack_a.pop()
        return "".join(stack_a)