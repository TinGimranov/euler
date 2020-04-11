min = 100
max = 1000


# Функция возвращает True, если строка явялется палиндромом
def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


max_palindrome = 0
for i in range(min, max):
    for j in range(i, max):
        n = i * j
        if is_palindrome(str(n)):
            if max_palindrome < n:
                max_palindrome = n
                print(f"{i} * {j} = {n}")
print(max_palindrome)
