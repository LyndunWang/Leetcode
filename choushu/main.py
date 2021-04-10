"""

解题思路：
0和负数直接返回false,1直接返回true
其他的数字使用2或3或5不断的做求余为0算法，如果最后整除到商值为1则就返回true
如果不能被求余为0立即就返回false

"""
class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        if n == 1:
            return True
        else:
            while 1:
                if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
                    # 能够被整除
                    if n % 2 == 0:
                        n = (n / 2)
                    elif n % 3 == 0:
                        n = (n / 3)
                    elif n % 5 == 0:
                        n = (n / 5)

                    if n == 1:  # 如果获取得的商值是1了
                        return True
                        break
                    elif n == 7:
                        return False
                        break
                else:
                    return False  #-2147483646
                    break
