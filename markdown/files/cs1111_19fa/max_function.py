def get_max_3(a, b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return a  # bug: should return c


def get_max_2(a, b):
    return (a + b + abs(a-b)) / 2


print(get_max_3(3, 2, 1))
print(get_max_3(1, 2, 3))
print(get_max_2(3, 2))
