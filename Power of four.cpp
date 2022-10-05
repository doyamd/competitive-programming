class Solution {
public:
    bool isPowerOfFour(int n) {
        int x=n;
    int power;
    bool poww=true;
      int count=0;
      if (x==1)
        return poww;
      else{
       while(x%4==0&&x>0){
           x=x/4;
           count++;
       }
          
     power=pow(4,count);
          cout<<power;
      if (count>0 && power==n)
        return poww;
       else 
        return !poww;
     
        }
    }
};
