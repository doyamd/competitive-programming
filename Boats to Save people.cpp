class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
      int l=0, r=people.size()-1,ans=0;
        sort(people.begin(),people.end());
        int k= limit;
        if(k==0) return 0;
        if(people.size()==0) return 0;
        while(l<=r){
            
            if(people[l]+people[r]<=k&&l!=r){
               ans++;
                l++; r--;
            }
            else {r--;ans++;}
        }
        return ans;
    }
};
