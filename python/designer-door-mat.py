"""
9 x 27
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
(N, M) = [int(x) for x in "9 27".split()]

for i in range(N):
    midPoint = int(N/2+N%2) - 1
    if i <= midPoint:
        genDoorLine(N,i)
    else:
        genDoorLine(N,N-i-1)


def genDoorLine(N,numRow):
    strLine = ""
    midPoint = int(N/2+N%2)
    iPos = numRow

    for i in range(N):
        iMidPos = midPoint-1
        if  iPos == midPoint-1:
            if i == (iMidPos - 1):
                strLine += "-WE"
            elif i == (iMidPos + 1):
                strLine += "ME-"
            elif i == iMidPos:
                strLine += "LCO"
            else:
                strLine += "---"
        elif i == iMidPos:
            strLine += ".|."
        elif i >= (iMidPos - iPos) and i <= (iMidPos + iPos):
            strLine += ".|."
        else:
            strLine += "---"
    print(strLine)


a = "------.|..|..|..|..|..|..|.------"
i = 0
for _ in range(11):
    print(a[i:i+3])
    i+=3
