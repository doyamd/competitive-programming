class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small = 0
        large = len(numbers)-1
        ans = [0,0]
        while small < large:
            if numbers[small] + numbers[large] > target:
                large -= 1
            elif numbers[small] + numbers[large] < target:
                small += 1
            else:
                ans[0] = small+1
                ans[1] = large+1
                break
        return ans