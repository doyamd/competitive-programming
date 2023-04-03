class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr,low,high):
            pivot = arr[high]
            i = low - 1
            for j in range(low,high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i],arr[j] = arr[j],arr[i]
            i += 1
            (arr[i],arr[high]) = (arr[high],arr[i])
            
            return i

        def quick(arr,low,high):
            if low < high:
                part = partition(arr,low, high)
                quick(arr,low,part-1)
                quick(arr,part+1,high)
        quick(nums,0,len(nums)-1)
        #print(nums)
        return (nums[-1*k])