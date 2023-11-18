class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        appear = ceil(len(nums)//3)
        count = Counter(nums)
        visited = set()
        for i in nums:
            if count[i] > appear and i not in visited:
                visited.add(i)
                ans.append(i)
        return ans
        