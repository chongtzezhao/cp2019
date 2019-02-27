import calendar
c=calendar.TextCalendar(calendar.SUNDAY)
year=eval(input("Enter year: "))
month=eval(input("Enter month: "))
days=0
for i in c.itermonthdays(year, month):
    if i!=0:
        days+=1

print(days)
