class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        while k >0:
            key = nums.pop()
            nums.insert(0,key)
            k -= 1
        """
        if k>len(nums): k = k%len(nums)
        last = nums[len(nums)-k:]
        first = nums[:len(nums)-k]
        i = 0
        for j in range(len(last)):
            nums[i] = last[j]
            i += 1
        for j in range(len(first)):
            nums[i] = first[j]
            i += 1    
        
            
                
            
            
        