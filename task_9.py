# Ответ 200 + 375 + 425 = 31_875_000
# 40000 + 140625 = 180625
N = 1000


def calculate():
    for a in range(1, N + 1):
        for b in range(a + 1, N + 1):
            for c in range(b + 1, N + 1):
                if a + b + c == N and a ** 2 + b ** 2 == c ** 2 and a < b < c:
                    return f"{a} * {b} * {c}", str(a * b * c)


if __name__ == "__main__":
    numbers, mult = calculate()
    print(f"{numbers} = {mult}")
