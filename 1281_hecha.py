class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = str(n)
        mult = 1
        sum = 0

        for i in a:
            mult *= int(i)
            sum += int(i)
        return mult - sum



