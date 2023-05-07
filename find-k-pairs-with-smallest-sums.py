class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(nums1)):
           sums = nums1[i] + nums2[0]
           heappush(heap,(sums,i,0))
           
        ans = []

        while heap and len(ans) < k:
            sums, i,j = heappop(heap)
            ans.append([nums1[i],nums2[j]])
            if j < len(nums2) - 1:
                sums = nums1[i] + nums2[j+1]
                heappush(heap,(sums,i,j+1))
        return ans