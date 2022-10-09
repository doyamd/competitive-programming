class Solution {
public:
    int evalRPN(vector<string>& tokens) {
       stack<int> st;
       for(auto& t : tokens) 
            if(t=="+"||t=="-"||t=="*"||t=="/"){
                long a =st.top(); st.pop();
                long b =st.top(); st.pop();
                if(t=="+") a = b+a;
                if(t=="-") a = b-a;   
                if(t=="*") a = b*a;
                if(t=="/") a = b/a;
                st.push(a);
            }
            else st.push(stoi(t));  
      return st.top(); 
    }
};

 
