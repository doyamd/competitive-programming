#https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    i=0
    ans=''
    while i<len(string):
        ans+=string[i]
        if (i+1)%max_width==0:
           ans+='\n'
        i+=1
    return ans
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
