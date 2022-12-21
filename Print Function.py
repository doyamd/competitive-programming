#https://www.hackerrank.com/challenges/python-print/
def solve(n):
    ans=''
    for x in range(1,n+1):
       ans+=str(x)
    return ans
    
if __name__ == '__main__':
    n = int(input())
    print(solve(n))
