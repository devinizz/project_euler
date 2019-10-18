def daysInYear(year):
  def february(year):
    return 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28 
  return [31, february(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 1
for i in daysInYear(1900):
  day += i
  day %= 7

ans = 0
for y in range(1901, 2001):
  for i in daysInYear(y):
    if day == 0:
      ans += 1
    day += i
    day %= 7

print(ans)
