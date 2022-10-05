class Solution {
public:
    int pivotIndex(vector<int>& nums) {
       
int leftSum = 0;
        int rightSum = 0;
        for (int i = 1; i < nums.size(); i++) {
            rightSum += nums[i];
        }
        if (rightSum == 0) {
            return 0;
        }
        for (int i = 1; i < nums.size(); i++) {
            leftSum += nums[i-1];
            rightSum -= nums[i];
            if (leftSum == rightSum) {
                return i;
            }
        }
        if (leftSum == 0) {
            return 0;
        }
        return -1;
        
    }
};
