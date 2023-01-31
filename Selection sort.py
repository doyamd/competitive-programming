#https://practice.geeksforgeeks.org/problems/selection-sort/1
#User function Template for python3

class Solution: 
    def selectionSort(self, arr,n):
        #code here
        for i in range (len(arr)):
            mini = arr[i]
            indx = i
            for j in range (i+1,len(arr)):
                if mini > arr[j]:
                    mini = arr[j]
                    indx = j
            arr[i], arr[indx] = arr[indx], arr[i]
