class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = defaultdict(int)
        arr = []
        def getPow(num):
            count = 0
            while num != 1:
                if num %2 == 0:
                    num = num//2
                else:
                    num = (num * 3) + 1
                count += 1
            d[num] = count
            return count
        
        for num in range(hi,lo-1,-1):
            # print(num)
            if num == 1:
                arr.append([0,num])
            elif d[num] != 0:
                arr.append([d[num],num])
            else:
                arr.append([getPow(num),num])
        arr.sort()
        # print(arr)
        return arr[k-1][1]


        
            
        