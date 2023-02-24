#https://codeforces.com/gym/424075/problem/B
test = int(input())
for index in range(test):
    ans = set()
    result = []
    string = input()
    if len(string) == 1:
        print(string)
    else:
        i = 0
        j=1
        while i < len(string) and j < len(string):
            if string[i] == string [j]:
                i += 2
                j += 2
            else:
                
                    ans.add(string[i])
                    i += 1
                    j += 1
        if j > len(string)-1 and i ==len(string)-1 :
            ans.add(string[i])
        for k in ans:
            result.append(k)
        result.sort()

        
        print("".join(result))
