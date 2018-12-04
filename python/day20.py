#!/bin/python3
import sys

"""
Bubble sort method
"""
n = int("3".strip())
a = list(map(int, "3 2 1".strip().split(' ')))
#a = list(map(int, "1 2 3".strip().split(' ')))

iSwaps = 0
for _ in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:
            iTemp=a[j+1]
            a[j+1]=a[j]
            a[j]=iTemp
            iSwaps+=1

print("Array is sorted in %s swaps." % iSwaps)
print("First Element: %s" % a[0])
print("Last Element: %s" % a[len(a)-1])
