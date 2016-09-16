# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).

def febDays(year):
    feb_day = 28
    if year%100!=0 and year%4==0:
        feb_day=29
    if year%400==0:
        feb_day=29
    if year%100==0 and year%400!=0:
        feb_day=28
    return feb_day

def daysofMonth(year,month):
    day="Wrong month"
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = 31
    else:
        if month == 2:
            day=febDays(year)
        else:
            if month == 4 or month == 6 or month == 9 or month == 11:
                day = 30
            else:
                day= "Wrong month"
    return day

def addDays(year,month):
    yCnt = year
    mCnt = 1
    dCnt=0
    while mCnt<=12:
        day = daysofMonth(yCnt,mCnt)
        dCnt= dCnt + day
        mCnt+=1
    else:
        return dCnt

def lastYearDays(year2, month2, day2):
    dCnt=0
    month=1
    while month < month2:
        dCnt = dCnt + daysofMonth(year2, month)
        month += 1
    else:
        dCnt = dCnt + day2
        return dCnt


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    yCnt=year1+1
    mCnt=month1
    dCnt=0

    # add all days except the fist year
    if year1==year2:
        dCnt = lastYearDays(year2, month2, day2)-1
        return dCnt
    else:
        while yCnt<year2:
            dCnt = dCnt+addDays(yCnt,mCnt)
            yCnt+=1
        else:
            dCnt = dCnt + lastYearDays(year2, month2, day2)

            # Calculate the days born in firs year
            month=1
            notBorn=0
            # Calculate days passed without being born
            while month < month1:
                notBorn = notBorn + daysofMonth(year1,month)
                month +=1
            else:
                notBorn = notBorn + day1
            # Delete the days not born from all first year days
            daysFirstYear = addDays(year1, 12) - notBorn

            # Add first year days born to the all others
            allDays = daysFirstYear + dCnt
            return allDays

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()
