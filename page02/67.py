from functools import reduce

f = open('67.txt')
t = f.read()
t = list(map(lambda x: list(map(int, x.split())),
      filter(lambda x: len(x) != 0, t.split('\n'))))

print(max(reduce(lambda x, y: list(map(lambda a, b: a + b, map(max, [0] + x, x + [0]), y)), t)))
