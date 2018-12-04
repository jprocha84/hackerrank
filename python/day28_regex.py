#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
#   N = int(input())
#
#   for N_itr in range(N):
#       firstNameEmailID = input().split()
#
#       firstName = firstNameEmailID[0]
#
#       emailID = firstNameEmailID[1]

    N = 6
    arrInputs = [
       "riya riya@gmail.com",
       "julia julia@juliaa.me",
       "julia sjulia@gmail.com",
       "julia julia@gmail.com",
       "samantha samantha@gmail.com",
       "tanya tanya@gmail.com"
    ]

    lstNames = []
    for i in range(N):
        firstNameEmailID = arrInputs[i].split()
        
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        m = re.search('(.*@gmail.com$)', emailID)

        if m is not None:
            lstNames.append(firstName)

    for name in sorted(lstNames):
        print(name)



