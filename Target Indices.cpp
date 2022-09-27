class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        
        int temp;
   
   
    vector<int> intVector;
    int n= nums.size();

    for(int i=1;i<n;i++){
        for(int j=0;j<(n-i);j++){
            if(nums[j]>nums[j+1]){
                temp=nums[j];
                nums[j]=nums[j+1];
                nums[j+1]=temp;
            }
        }
    }
     for( int i=0; i < n; i++) {
         if(nums[i]==target)
           intVector.push_back (i);

        }
   return intVector; 
    }
    
};
