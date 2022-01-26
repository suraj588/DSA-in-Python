# Constraints: m and n should be positive

fm = []                             # factors of m
fn = []                             # factors of n
cf = []                             # common factors of m and n

def gcd(m,n):
  for i in range(1,m+1):
    if m%i == 0:
      fm.append(i)
  for j in range(1,n+1):
    if n%j == 0:
      fn.append(j)
  for factor in fm:
    if factor in fn:
      cf.append(factor)
  print(cf[-1])                     # largest common factor
  return cf[-1]

gcd(56,84)
