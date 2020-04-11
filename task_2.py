# Дано
limit = 4_000_000

n1 = 1
n2 = 2
s = 0

while n2 <= limit:
    # if n2 % 2 == 0:
    #     s += n2
    temp = n2 + n1
    n1 = n2
    n2 = temp
print(s)
