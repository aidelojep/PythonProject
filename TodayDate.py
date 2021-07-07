from datetime import timedelta, datetime


now = datetime.now()
print("Today's date is: " + str(now))

print("One year from now will be: " + str(now + timedelta(days=365)))
print("In two days and three weeks , it will be :" + str(now + timedelta(days=2, weeks=20)))
t= datetime.now() - timedelta(weeks=1)
s=t.strftime("%A %B %d, %Y")
print("One week ago it was: " + s)