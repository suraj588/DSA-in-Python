# Using Eucledian's remainder algorithm: gcd(m, n) = gcd(n, m-n)
# No recursion

def gcd(m, n):
  if m < n:
    (m, n) = (n, m)

  remainder = m % n
  while remainder != 0:
    (m, n) = (n, remainder)
    remainder = m % n
  print(n)
  return n
