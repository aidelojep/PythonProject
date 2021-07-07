from datetime import time
from datetime import date
from datetime import datetime


def main():
   today = date.today()
   print("Today date is:", today)

   print("Date components: ", today.day, today.month, today.year)
   print("Today's weekday number is:", today.weekday())

   days=["mon","tues","wed","Thurs","Fri","sat"]
   print("Today's weekday is: ", days[today.weekday()])


if __name__ == "__main__":
    main()