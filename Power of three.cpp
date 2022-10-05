class Solution {
public:
    bool isPowerOfThree(int n) {
        int x=n;
    int power;
    bool poww=true;
      int count=0;
      if (x==1)
        return poww;
      else{
       while(x%3==0&&x>0){
           x=x/3;
           count++;
       }
          
     power=pow(3,count);
          cout<<power;
      if (count>0 && power==n)
        return poww;
       else 
        return !poww;
     
        }
    }
};
