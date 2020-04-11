s = 0


def fibonacchi():
    a, b = 1, 2
    while a <= 4_000_000:
        yield a
        a, b = b, a + b


generator = fibonacchi()
for i in generator:
    if i % 2 == 0:
        s += i
print(s)
