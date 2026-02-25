class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        counter = 0
        for hr in hours:
            if hr >= target:
                counter += 1
        return counter
