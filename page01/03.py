from prime import Prime

num = 600851475143
for i in Prime.prime():
  if i ** 2 > num:
    break
  while num % i == 0:
    num //= i
  if num == 1:
    num = i
    break
    
print(num)
