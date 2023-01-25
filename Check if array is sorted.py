#https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return 0
        return 1
