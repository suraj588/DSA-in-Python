# Using Eucledian's algorithm: gcd(m, n) = gcd(n, m-n)
# No recursion

def gcd(m, n):
  if m < n:
    (m, n) = (n, m)
  
  while m % n != 0:
    diff = m - n
    (m, n) = (max(diff, n), min(diff, n))
  
  print(n)
  return n
