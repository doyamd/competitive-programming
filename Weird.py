#https://www.hackerrank.com/challenges/py-if-else/


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    else:
        if n<=2 and n>=5:
            print("Not Weird")
        elif n<=20 and n>=6:
            print("Weird")
        else:
            print("Not Weird")
        
