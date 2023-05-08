#TASK 2

def is_leap_year(year):
     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_day_of_week(date):
     days_per_month = (31, 28 + is_leap_year(int(date[:4])), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
     days_since_jan1st = sum(days_per_month[:int(date[5:7])-1]) + int(date[-2:])
     day_of_week_index = (days_since_jan1st - 1) % 7
     days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
     return days_of_week[day_of_week_index]

date = input(" Enter a date (YYYY-MM-DD): ")
day_of_week = get_day_of_week(date)
print(f"The day of the week for {date} is {day_of_week}.")