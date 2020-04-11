# Ответ: 232_792_560

limit = 20

# Построим список всех делителей
divisors = [d for d in range(2, limit + 1)]

n = limit * 2
while True:
    status = True
    for d in divisors:
        if n % d != 0:
            status = False
            break
    if status:
        break
    else:
        n += 1
print(n)
