class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        d =defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                    if nums1[i] == nums2[j]:
                        d[(i,j)] = 1 + d[(i-1,j-1)]
        if not d.values():
            return 0
        return max(d.values())
                    

    
        # ans = 0
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         temp = j
        #         index = i
        #         while index+1 < len(nums1) and temp+1 < len(nums2) and nums1[index+1] == nums2[temp+1] and nums1[index] == nums2[temp]:
        #             temp += 1
        #             index += 1
        #         ans = max(ans,(index-i+1))
        #         if ans == len(nums1):
        #             return ans

        # return ans
      
        