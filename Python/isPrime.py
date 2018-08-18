from math import sqrt

def is_prime(x):
  if x <= 1:
    return False
  elif x == 2:
    return True
  elif x % 2 == 0:
    return False
  for i in range(3, int(sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True


print(is_prime(71))
