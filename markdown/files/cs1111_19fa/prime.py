i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1

print("==================")

for y in range(2, 1001):
    is_prime = True
    loop_end = int(y ** 0.5) + 1
    for i in range(2, loop_end):
        if y % i == 0:
            is_prime = False
            break
    if is_prime:
        print(y)
