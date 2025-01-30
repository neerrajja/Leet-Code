class Solution:
    def reverse(self, x: int) -> int:
        minimum = -2**31
        maximum = 2**31 - 1
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            rem = x % 10
            reverse = (reverse * 10) + rem
            x = x// 10

            if reverse < minimum or reverse > maximum:
                return 0
        result = sign * reverse
        return result


        