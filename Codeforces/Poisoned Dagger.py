#https://codeforces.com/gym/433454/problem/E
test = int(input())

for t in range(test):
    attack, damage = map(int,input().split())
    nums = list(map(int,input().split()))
    def is_true(k):
        result = 0
        for i in range(len(nums)-1):
            result += min(k, nums[i+1] - nums[i])
        result += k   
        return result >= damage
    ans = 0
    l = 0
    r = damage
    while l<= r:
        mid = (l + r) // 2

        if is_true(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)
