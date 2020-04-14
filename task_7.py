# Ответ: 104_743

limit = 10_001


def is_prime(_n):
    d = 2
    while _n % d != 0:
        d += 1
    return d == _n


def detect_prime_number():
    num = 2
    amount = 0
    while True:
        if is_prime(num):
            amount += 1
            print(f"{amount} простое число: {num}")
            if amount == limit:
                break
        num += 1


if __name__ == "__main__":
    detect_prime_number()
