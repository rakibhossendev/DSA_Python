class Solution:
    def tribonacci(self, n: int) -> int:
        meno = {}
        def f(n):
            if n in meno:
                return meno[n]
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            meno[n] = f(n-1)+f(n-2)+f(n-3)
            return meno[n]
        return f(n)
