class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector <string> answer;
        string x;
    for( int i=1;i<=n;i++){

        if((i%3==0)&&(i%5==0))
            x = "FizzBuzz";
        else if(i%3==0)
            x ="Fizz";
        else if (i%5==0)
            x ="Buzz";
        else{
            x =to_string(i);
            }
     answer.push_back(x);

    }


    return answer;
        
    }
};
