import math

# lcm and gcd

def gcd(a,b):
  if a == 0: return b
  return gcd(b%a, a)

def lcm(a,b):
  prod = a*b
  gc = gcd(a,b)
  return prod // gc


# is a prime number

def isPrime(n):
  if n == 0 or n == 1: return False
  if n == 2 or n == 3: return True
  if n%2 == 0 or n%3 == 0: return False
  for i in range(5, int(math.sqrt(n)) + 1):
    if n%i == 0 or n%(i+2): return False
    
  return True
