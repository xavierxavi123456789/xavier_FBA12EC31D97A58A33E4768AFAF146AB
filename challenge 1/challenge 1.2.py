year = int(input("enter the year:"))
if (year % 4 ==0 and year % 100!=0) or (year % 400==0):
  return True
else:
  return false
year=int(input("enteer the year:"))
if is_leap_year(year):
  print(year,"is a leap year.")
else:
  print(year,"is not a leap year.")
  