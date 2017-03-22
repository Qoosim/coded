def fibonacci(n, a = 0, b = 1):

    if b > n:
      return a
    tmp = a
    a = b
    b = b + tmp

    return fibonacci(n, a, b)

print(fibonacci(150))
