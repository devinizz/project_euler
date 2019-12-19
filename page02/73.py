from math import gcd
print(sum(map(lambda x: len(list(filter(lambda y: gcd(y, x) == 1, 
                                        range(x // 3 + 1, (x + 1) // 2)))), 
              range(1, 12001))))
