#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getUniqueCharacter' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getUniqueCharacter(s):
    lst = list(s)
    temp=dict()
    for i in range(len(lst)):
        if (lst[i] not in temp):
            temp[lst[i]] = 1
        else:
            temp[lst[i]] += 1

    min_key = [k for k, v in temp.items() if v == 1]
    if (len(min_key) == 0):
        print(-1)
    else:
        print(lst.index(min_key[0])+1)


if __name__ == '__main__':
   #fptr = open(""./output.txt", 'w')
   fptr = sys.stdout
  #s = "falafal"
   s = input()

   result = getUniqueCharacter(s)


   #fptr.write(str(result) + '\n')

   fptr.close()
