class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def func(s,left,right):
            if left >= right:
                return
            s[left],s[right] = s[right],s[left]
            func(s,left+1,right-1)

        func(s,0,len(s) -1)
        return s
