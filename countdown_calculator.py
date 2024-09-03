from datetime import date

date1 = list(map(int,input("Enter the first date (YYYY-MM-DD) : ").split("-")))
first_date = date(date1[0],date1[1],date1[2])

date2 = list(map(int,input("Enter the second date (YYYY-MM-DD) : ").split("-")))
second_date = date(date2[0],date2[1],date2[2])

print(f"Difference in days = {abs(second_date-first_date).days}")
