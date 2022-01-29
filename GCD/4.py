# Using Eucledian's algorithm: gcd(m, n) = gcd(n, m-n)

def gcd(m, n):
  if n > m:
    (m, n) = (n ,m)

  if m % n == 0:                               # Breakpoint
    print(n)
    return n
  
  diff = m - n
  return gcd(max(diff, n), min(diff,n))        # Recursive technique
