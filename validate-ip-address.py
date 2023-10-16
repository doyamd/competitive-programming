class Solution:
    def validIPAddress(self, query: str) -> str:
        n = len(query)
        self.v4,self.v6 = True,True
        alpha = 'abcdefABCDEF'
        num = '0123456789'
        if not query or ((query[-1] not in alpha) and (query[-1] not in num)):
            return 'Neither'
        def identify(i):
            s = ''
            if i >= n:
                return
            while i < n and query[i]!= '.' and query[i] != ':':
                s += query[i]
                if query[i] in alpha:
                    self.v4 = False
                if query[i] not in alpha and query[i] not in num:
                    self.v4,self.v6 = False,False
                i += 1
            # print(s)
            if s and (s[0] == '0' and len(s) > 1) or (not s.isnumeric()) or (0 > int(s)) or (int(s) > 255):
                self.v4 = False
            if len(s) < 1 or len(s) > 4:
                self.v6 = False 
            if i < n:
                # print(query[i])
                if query[i] == '.':
                    self.v6 = False
                else:
                    self.v4 = False
            # print(self.v4,self.v6,s)
            return identify(i+1)
        identify(0)
        # print(self.v4,self.v6)
        if self.v4:
            arr = query.split('.')
            if len(arr) > 4 or len(arr) < 4:
                return 'Neither' 
            return 'IPv4'
        elif self.v6:
            arr = query.split(':')
            if len(arr) > 8 or len(arr) < 8:
                return 'Neither' 
            return 'IPv6'
        else:
            return 'Neither'