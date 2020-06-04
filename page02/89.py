mm = {'IIII': 2, 'VIIII': 1, 'XXXX': 2, 'LXXXX': 1, 'CCCC': 2, 'DCCCC': 1}
def count(x):
  return sum(map(lambda p: mm[p] if x.find(p) != -1 else 0, mm))

f = open('89.txt', 'r')
roman = list(filter(lambda x: len(x) != 0, f.read().split('\n')))
print(sum(map(count, roman)))
