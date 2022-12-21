#https://www.hackerrank.com/challenges/python-string-split-and-join/
def split_and_join(line):
    a= list(line.split(' '))
    ans=''
    ans='-'.join(a)
    return ans

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
