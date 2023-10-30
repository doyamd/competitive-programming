class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(i,j):
            while i <= j:
                mid = (i+j+1)//2
                if target == nums[mid]:
                    return mid
                elif nums[i] <= nums[mid]:
                    if target >= nums[i] and target < nums[mid]:
                        j = mid - 1
                    else:
                        i = mid + 1
                else:
                    if target <= nums[j] and target > nums[mid]:
                        i = mid + 1
                    else:
                        j = mid - 1
            # if i < len(nums) and nums[i] == target:
            #     return i
            # if j > 0 and nums[j] == target:
            #     return j
            return -1
        return search(0,len(nums)-1)
                
                



        