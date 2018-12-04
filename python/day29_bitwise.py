#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

#       lstBitWise = [0]
#       for i in range(1,n+1):
#           for j in range(i+1,n+1):
#               iBitWise = i&j
#               print(i,j,bin(i),bin(j),iBitWise, bin(iBitWise))
#               if iBitWise < k and iBitWise>0:
#                   lstBitWise.append(iBitWise)
#       print(max(lstBitWise))
#
        """
        2-2
        """
        print(k-1 if ((k-1) | k) <= n else k-2)
