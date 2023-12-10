class Solution:
    def countTime(self, time: str) -> int:
        num1, num2 = time.split(':')
        sums = 1
        if num1[0] == '?' and num1[1] == '?':
            sums *= 24
        elif num1[0] == '?' and int(num1[1]) < 4:
            sums *= 3
        elif num1[0] == '?' and int(num1[1]) >= 4:
            sums *= 2
        elif int(num1[0]) < 2 and num1[1] == '?':
            sums *= 10
        elif int(num1[0]) >= 2 and num1[1] == '?':
            sums *= 4
        if num2[0] == '?':
            sums *= 6
        if num2[1] == '?':
            sums *= 10
        return sums

        