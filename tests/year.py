import pandas as pd

thangdu = [1, 3, 5, 7, 8, 10, 12]
thangthieu = [4, 6, 9, 11]
number = ''
dtc = []
b = 0
a = 0
for year in range(0000, 2020+1):
    for month in range(1, 12+1):
        if month == 2 and year//4:
            day = 29
        elif month in thangdu:
            day = 31
        elif month in thangthieu:
            day = 30
        else:
            day = 28
        for eachday in range(1, day+1):
            date = str(eachday) + ',' + str(month) + ',' + str(year)
            total = sum([int(a) for a in str(eachday)]) + sum([int(b) for b in str(month)]) + sum([int(c) for c in str(year)])
            if total == 22:
                number = '22/4'
                a +=1
            else:
                number = str(sum(int(d) for d in str(total)))
            dtc.append({'date': date, 'number': number})
            b = b+1
print(a/b)
# df = pd.DataFrame(dtc)
# df.to_csv('J2team.csv')

