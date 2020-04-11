limit = 600_851_475_143
n = int(limit / 2)
print(f"Старт: {n}")

while n >= 1:
    print(f"Теккущее число {n}")
    if limit % n == 0:
        print(f"Найденный делитель: {n}")
        break
    n -= 1
