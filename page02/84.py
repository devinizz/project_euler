import random

board = """GO	A1 CC1 A2 T1 R1 B1 CH1 B2	B3 JAIL
C1 U1 C2 C3 R2 D1 CC2 D2 D3
FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J
G1 G2 CC3 G3 R4 CH3 H1 T2 H2""".split()

position = 0
count = [0] * len(board)
double = 0
time = 999999

def goto(label):
  global position
  while board[position].find(label) != 0:
    position += 1
    position %= len(board)

def event():
  global position
  if board[position].find("G2J") == 0:
    goto("JAIL")
  elif board[position].find("CC") == 0:
    ch = random.randint(1, 16)
    if ch == 1:
      goto("GO")
    elif ch == 2:
      goto("JAIL")
  elif board[position].find("CH") == 0:
    ch = random.randint(1, 16)
    if ch == 1:
      goto("GO")
    elif ch == 2:
      goto("JAIL")
    elif ch == 3:
      goto("C1")
    elif ch == 4:
      goto("E3")
    elif ch == 5:
      goto("H2")
    elif ch == 6:
      goto("R1")
    elif ch == 7:
      goto("R")
    elif ch == 8:
      goto("R")
    elif ch == 9:
      goto("U")
    elif ch == 10:
      position -= 3
      position %= len(board)
      event()


for i in range(time):
  count[position] += 1
  d1 = random.randint(1, 6)
  d2 = random.randint(1, 6)
  if d1 == d2:
    double += 1
    if double == 3:
      goto("JAIL")
      double = 0
      continue
  else:
    double = 0
  position += d1 + d2
  position %= len(board)
  event()
      
result = sorted(map(lambda x, y: [x,y], count, range(len(count))))
print('{:02}{:02}{:02}'.format(result[-1][1], result[-2][1], result[-3][1]), sep='')
