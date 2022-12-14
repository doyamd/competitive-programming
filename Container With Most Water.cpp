class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0,r=height.size()-1;
        int water=0,area=0;
        while(l<r){
            if(height[l]<height[r]){
                area=height[l]*(r-l);
                l++;
            }
        else{
            area=height[r]*(r-l);
            r--;
            }
        if(area>water)
            water=area;
        }
        return water;
    }
};
