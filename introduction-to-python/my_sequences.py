# Fibonacci sequence
def fibonacci(n):
    s = [0]
    a, b = 0, 1
    while len(s) < n:
        s.append(b)
        a, b = b, a + b
    return s


# Syracuse sequence
def syracuse(n):
    s = []
    u = n
    while u != 1:
        s.append(u)
        u = u // 2 if u % 2 == 0 else 3 * u + 1
    s.append(1)
    return s
