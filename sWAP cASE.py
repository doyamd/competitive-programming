#https://www.hackerrank.com/challenges/swap-case/
def swap_case(s):
    new=""
    for ch in s:
         if(ch>='A' and ch<='Z'):
            new+=ch.lower() 
         elif(ch>='a' and ch<='z'):
            new+=ch.upper()
         else:
            new+=ch
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
