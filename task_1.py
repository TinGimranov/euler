# Дано

limit = 1000
k = (3, 5)

# Решение
s = 0
for i in range(limit):
    for _k in k:
        if i % _k == 0:
            s += i
            break
print(s)
