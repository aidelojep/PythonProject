import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
sc = c.formatmonth(2018, 7, 0, 0)
print(sc)

p = calendar.HTMLCalendar(calendar.MONDAY)
hc = p.formatmonth(2020, 7)
print(hc)

for i in c.itermonthdays(2021, 8):
    print(i)