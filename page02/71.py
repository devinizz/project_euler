from fractions import Fraction

print(min(filter(lambda x: x[0] != 0, map(lambda x: [Fraction(3, 7) - x, x.numerator], 
    map(lambda x: Fraction(x * 3 // 7, x), range(1, 1000001)))))[1])
