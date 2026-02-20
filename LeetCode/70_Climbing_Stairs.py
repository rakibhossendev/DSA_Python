class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}  # dictionary to store already computed results
        
        def f(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:  
                return memo[n]
            
            memo[n] = f(n-1) + f(n-2)
            return memo[n]
        
        return f(n)

sol = Solution()
print(sol.climbStairs(45))
