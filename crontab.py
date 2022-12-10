import calendar
import datetime

inputs = input().split()
n = int(inputs[0])
s = inputs[1]
f = inputs[2]
syear = int(s[:4])
smonth = int(s[4:6])
sday = int(s[6:8])
shour = int(s[8:10])
smin = int(s[10:12])
fyear = int(f[:4])
fmonth = int(f[4:6])
fday = int(f[6:8])
fhour = int(f[8:10])
fmin = int(f[10:12])
sdate = datetime.datetime(syear, smonth, sday, 0, 0)
sdate1 = datetime.datetime(syear, smonth, sday, shour, smin)
fdate = datetime.datetime(fyear, fmonth, fday, fhour, fmin)
fdate1 = datetime.datetime(fyear, fmonth, fday, fhour, fmin)
commands = []
strmap = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
          "Nov": 11, "Dec": 12, "Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 0}
for i in range(n):
    temp = []
    cmd = input().split()
    for part in cmd:
        partlst = part.split(",")
        temp.append(partlst)
    minlst = []
    for _ in temp[0]:
        if "-" in _:
            m1, m2 = map(int, _.split('-'))
            for __ in range(m1, m2 + 1):
                minlst.append(__)
        elif _ == '*':
            for __ in range(60):
                minlst.append(__)
        else:
            minlst.append(int(_))
    minlst=list(set(minlst))
    minlst.sort()
    temp[0] = minlst
    hourlst = []
    for _ in temp[1]:
        if "-" in _:
            h1, h2 = map(int, _.split('-'))
            for __ in range(h1, h2 + 1):
                hourlst.append(__)
        elif _ == '*':
            for __ in range(24):
                hourlst.append(__)
        else:
            hourlst.append(int(_))
    hourlst=list(set(hourlst))
    hourlst.sort()
    temp[1] = hourlst
    commands.append(temp)
while sdate <= fdate:
    prlst = []
    for cmd in commands:
        day = cmd[2]
        flag3 = 0
        if day[0] == '*':
            flag3 = 1
        for d in day:
            if "*" in d:
                flag3 = 1
                break
            if '-' in d:
                if sdate.day <= int(d.split('-')[1]) and sdate.day >= int(d.split('-')[0]):
                    flag3 = 1
            else:
                if sdate.day == int(d):
                    flag3 = 1
        month = cmd[3]
        flag4 = 0
        if month[0] == '*':
            flag4 = 1
        for m in month:
            if "*" in m:
                flag4 = 1
                break
            if '-' in m:
                m1, m2 = m.split("-")
                m1 = m1.lower().capitalize()
                m2 = m2.lower().capitalize()
                if m1[0] <= 'Z' and m1[0] >= 'A':
                    m1 = strmap[m1]
                else:
                    m1 = int(m1)
                if 'Z' >= m2[0] >= 'A':
                    m2 = strmap[m2]
                else:
                    m2 = int(m2)
                if m2 >= sdate.month >= m1:
                    flag4 = 1
            else:
                m=m.lower().capitalize()
                if 'Z' >= m[0] >= 'A':
                    m = strmap[m]
                else:
                    m = int(m)
                if sdate.month == m:
                    flag4 = 1
        weekday = cmd[4]
        flag5 = 0
        if weekday[0] == '*':
            flag5 = 1
        for w in weekday:
            if "*" in w:
                flag5=1
                break
            if '-' in w:
                w1, w2 = w.split("-")
                w1 = w1.lower().capitalize()
                w2 = w2.lower().capitalize()
                if w1[0] <= 'Z' and w1[0] >= 'A':
                    w1 = strmap[w1]
                else:
                    w1 = int(w1)
                if w2[0] <= 'Z' and w2[0] >= 'A':
                    w2 = strmap[w2]
                else:
                    w2 = int(w2)
                if (sdate.weekday() + 1) % 7 <= w2 and (sdate.weekday() + 1) % 7 >= w1:
                    flag5 = 1
            else:
                w=w.lower().capitalize()
                if w[0] <= 'Z' and w[0] >= 'A':
                    w = strmap[w]
                else:
                    w = int(w)
                if (sdate.weekday() + 1) % 7 == w:
                    flag5 = 1
        if flag3 and flag4 and flag5:
            for hour in cmd[1]:
                for min in cmd[0]:
                    if datetime.datetime(sdate.year, sdate.month, sdate.day, int(hour), int(min)) < sdate1:
                        continue
                    if datetime.datetime(sdate.year, sdate.month, sdate.day, int(hour), int(min)) >= fdate1:
                        continue
                    pr = ""
                    pr += str(sdate.year)
                    if sdate.month < 10:
                        pr += "0" + str(sdate.month)
                    else:
                        pr += str(sdate.month)
                    if sdate.day < 10:
                        pr += "0" + str(sdate.day)
                    else:
                        pr += str(sdate.day)
                    if hour < 10:
                        pr += "0" + str(hour)
                    else:
                        pr += str(hour)
                    if min < 10:
                        pr += "0" + str(min)
                    else:
                        pr += str(min)
                    prlst.append(pr + " " + cmd[5][0])
    prlst.sort(key=lambda t: t[:12])
    for _ in prlst:
        print(_)
    sdate += datetime.timedelta(days=1)