class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int l=nums.size();
        swaplable:
   for(int i=1;i<l-1;i++){
    if(nums[i]==(nums[i-1]+nums[i+1])/2)
        swap(nums[i],nums[i-1]);
       
   }
        for(int i=1;i<l-1;i++){
        if(nums[i]==(nums[i-1]+nums[i+1])/2)
            goto swaplable;
            }
return nums;
        
    }
};
