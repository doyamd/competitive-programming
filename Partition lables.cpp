class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> idx(26,0);
        for(int i=0;i<s.size();++i)
            idx[s[i]-'a']=i;
        vector<int>result;
        int start=0, end=0;
        for(int i=0;i<s.size();++i){
          end=max(end,idx[s[i]-'a']);
              if(end==i){
                  result.push_back((i-start)+1);
                  start=i+1;
              }
        }
        return result;
    }
};
