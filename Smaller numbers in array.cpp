class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        
     vector<int> ans;
    int l= nums.size();
    for(int i=0;i<l;i++)
    {
        int count=0;
        for(int j=0;j<l;j++)
        {
            if(nums[j]<nums[i])  count++;
        }
        ans.push_back(count);
    }
    return ans;
    }
};
