from datetime import timedelta, datetime

arrDate = [int(x) for x in "5 6 2015".split()]
#arrDateDue = [int(x) for x in "6 6 2015".split()]
arrDateDue = [int(x) for x in "6 6 2015".split()]

dtRec = datetime(arrDate[2],arrDate[1],arrDate[0])
dtDue = datetime(arrDateDue[2],arrDateDue[1],arrDateDue[0])

intDiffDays = (dtRec-dtDue).days

if intDiffDays < 0:
    intFine = 0 
elif dtRec.month == dtDue.month and dtRec.year == dtDue.year:
    intFine = intDiffDays * 15
elif dtRec.year == dtDue.year:
    intFine = (dtRec.month - dtDue.month)*500
else:
    intFine =  10000

print(intFine)
