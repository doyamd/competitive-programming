class Solution {
public:
    void sortColors(vector<int>& nums) {
         int temp,swp=0;
int l= nums.size();

    for(int i=1;i<l;i++){
        for(int j=0;j<(l-i);j++){
            if(nums[j]>nums[j+1]){
                temp=nums[j];
                nums[j]=nums[j+1];
                nums[j+1]=temp;
                swp++;
            }
        }

    }
    for(int i=0;i<l;i++)
    cout<<nums[i];
    }
};
