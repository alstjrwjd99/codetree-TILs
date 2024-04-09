from datetime import datetime

class Data:
    def __init__(self,date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
n = int(input())
wd = []
for _ in range (n):
    a = input().split()
    if a[2] == 'Rain':
        date1 = datetime.strptime(a[0], "%Y-%m-%d")
        wd.append(Data(date1,a[1],a[2]))
wd.sort(key = lambda x : x.date)
print(str(wd[0].date)[:10],wd[0].day,wd[0].weather)