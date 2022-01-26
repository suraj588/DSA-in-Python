# Constraint: m, n should be positive

def gcd(m,n):
  flag = 1                              # setting 1 as default value of gcd
  for i in range(min(m,n), 2, -1):
    if (m % i == 0) and (n % i == 0):
      print(i)
      return i
  print(flag)
  return flag
