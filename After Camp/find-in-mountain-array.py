# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        def finder(i,j):
            while i < j:
                mid = (i+j+1)//2
                center = mountain_arr.get(mid)
                print(i,j)
                if mid+1 < n and mid-1 >= 0:
                    left =  mountain_arr.get(mid-1)
                    right = mountain_arr.get(mid+1)
                elif mid == n-1:
                    return mid - 1
                elif mid == 0:
                    return mid + 1
                if center > left and center > right:
                    return mid
                elif center > left and center < right:
                    i = mid + 1
                elif center < left and center > right:
                    j = mid - 1
            return j
        def binary(i,j,is_right):
            while i+1 < j:
                mid = (i+j+1)//2
                center = mountain_arr.get(mid)
                if center == target:
                    return mid
                elif center < target:
                    if is_right:
                        j = mid - 1
                    else:
                        i = mid + 1
                elif center > target:
                    if is_right:
                        i = mid + 1
                    else:
                        j = mid - 1
            if 0 <= j < n and target == mountain_arr.get(j):
                return j
            elif 0 <= i < n and target == mountain_arr.get(i):
                return i
            return float('inf')
        main = finder(0,n-1)
        print(mountain_arr.get(main))

        if mountain_arr.get(main) == target:
            return main
        left = binary(0,main-1,False)
        right = binary(main+1,n-1,True)
        # print(left, right)
        if left == right == float('inf'):
            return -1
        return min(left,right)