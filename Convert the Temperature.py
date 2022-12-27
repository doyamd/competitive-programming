#https://leetcode.com/problems/convert-the-temperature/
class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans=list()
        Kelvin = celsius + 273.15
        Fahrenheit =celsius * 1.80 + 32.00

        ans.append(Kelvin)
        ans.append(Fahrenheit)

        return ans
