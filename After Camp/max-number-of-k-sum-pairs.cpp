class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
       unordered_map<int, int> numb;
        int ans = 0;
        for (int b : nums) {
            int a = k - b; 
            if (numb[a] > 0) {
                ans += 1;
                numb[a] -= 1;
            } else {
                numb[b] += 1;
            }
        }
        return ans;

    }
};