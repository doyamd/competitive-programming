#https://codeforces.com/gym/419351/problem/A
n=int(input())
i=0
ans=''
while i<n:
    words=input()
    ans+=words[0]
    ans+=words[1]
    ans+='... '
    print(ans+words+'?')
    ans=''
    i+=1
