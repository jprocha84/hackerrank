'''
Calculate Quartiles
'''
N = 9
lstObjs = [int(x) for x in "3 7 8 5 12 14 21 13 18".split()]
lstObjs = [int(x) for x in "3 7 8 5 12 14 21 13".split()]

N = len(lstObjs)
lstObjs.sort()
print(calcMedian(lstObjs))

def calcMedian(lstItems, N):
    return ((lstItems[int(N/2)-1]+lstItems[int(N/2)])/2) if N%2==0 else lstItems[int(N/2+N%2)-1]

# Get the median
Q2 = calcMedian(lstObjs, N)

# Calculate the Quartiles
lstQ1 = lstObjs[:int(N/2)]
if N%2 != 0:
    lstQ3 = lstObjs[int(N/2)+1:]
else:
    lstQ3 = lstObjs[int(N/2):]

Q1 = calcMedian(lstQ1, len(lstQ1))
Q3 = calcMedian(lstQ3, len(lstQ3))


'''
Calculate Interquartiles range
'''
# Sample input
N = 6
lstItems = [int(x) for x in "6 12 8 10 20 16".split()]
lstFreq = [int(x) for x in "5 4 3 2 1 5".split()]

lstS = []
for i in range(N):
    for _ in range(lstFreq[i]):
        lstS.append(lstItems[i])
lstS.sort()
iMidPoint = int(len(lstS)/2)
lstQ1 = lstS[:iMidPoint]
if iMidPoint%2 != 0:
    lstQ3 = lstS[int(iMidPoint)+1:]
else:
    lstQ3 = lstS[int(iMidPoint):]

Q1 = calcMedian(lstQ1, len(lstQ1))
Q3 = calcMedian(lstQ3, len(lstQ3))
numInterquartile = Q3 - Q1

print("%.1f" % numInterquartile)

'''
Calculate the standard deviation
'''
def calcMean(lstNumbers):
    N = len(lstNumbers)
    return sum(lstNumbers)/N

def calcSTD(lstNumbers):
    N = len(lstNumbers)
    mean = calcMean(lstNumbers)
    return (sum([(x - mean)**2 for x in lstNumbers])/N)**0.5

N = 5
lstNumbers = [int(x) for x in "10 40 30 50 20".split()]

# print(calcMean(lstNumbers))
print("%.1f" % calcSTD(lstNumbers))
