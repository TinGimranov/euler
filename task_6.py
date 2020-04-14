# Ответ: 25_164_150

N = 100


def compute():
    sum_sq = sum(i ** 2 for i in range(1, N + 1))
    sq_of_sum = sum(i for i in range(1, N + 1)) ** 2
    return sq_of_sum - sum_sq


if __name__ == "__main__":
    print(compute())
