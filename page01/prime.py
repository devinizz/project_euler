class Prime:
  p = [2, 3]
  def prime():
    p = Prime.p
    yield p[0]
    yield p[1]
    index = 2
    n = 5
    while True:
      if len(p) > index:
        n = p[index]
        yield p[index]
        index += 1
      else:
        for i in p:
          if n % i == 0:
            break
          if i ** 2 > n:
            p.append(n)
            yield n
            index += 1
            break
      n += 2
