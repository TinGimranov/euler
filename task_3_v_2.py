# Ответ 6_857

limit = 600_851_475_143
n = 2
print(f"Старт: {n}")


def is_prime(_n):
    d = 2
    while _n % d != 0:
        d += 1
    return d == _n


while n <= int(limit / 2):
    if limit % n == 0:
        _d = limit / n
        print(f"Найденный делитель: {_d}")
        if is_prime(_d):
            break
    n += 1
