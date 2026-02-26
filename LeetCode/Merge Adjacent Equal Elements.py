class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            current = num
            while stack and stack[-1] == current:
                current += stack.pop()
            stack.append(current)

        return stack
