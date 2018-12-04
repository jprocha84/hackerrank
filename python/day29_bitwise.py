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

        lstBitWise = []
        for i in range(1,n+1):
            for j in range(i,n+1):
                iBitWise = i&j
                if iBitWise < k and i!=j:
                    lstBitWise.append(iBitWise)
        print(max(lstBitWise))

