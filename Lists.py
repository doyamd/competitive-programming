#https://www.hackerrank.com/challenges/python-lists/problem/
if __name__ == '__main__':
    N = int(input())
    list_ans=[]
    for i in range(N):
        lis=list(input().split())
        if lis[0]=='insert':
            list_ans.insert(int(lis[1]),int(lis[2]))
        elif lis[0]=='append':
            list_ans.append(int(lis[1]))
        elif lis[0]=='pop':
            list_ans.pop()
        elif lis[0]=='remove':
            list_ans.remove(int(lis[1]))
        elif lis[0]=='sort':
            list_ans.sort()
        elif lis[0]=='reverse':
            list_ans.reverse()
        elif lis[0]=='print':
            print(list_ans)
