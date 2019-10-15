print("======Normal loop 0-5 (not including 5) =====")

for i in range(5):
    print(i)


print("======Normal loop 0-5 (not including 5) by steps of 2 =====")

for i in range(0, 5, 2):
    print(i)


print("======Reverse Loop 5 to 0 =====")

for i in range(5, -1, -1):
    print(i)


print("======Loop 0 to 5, break at 2 =====")

for i in range(0, 5):
    if i == 2:
        break
    print(i)

print("======Loop 0 to 5, continue at 2 =====")

for i in range(0, 5):
    if i == 2:
        continue
    print(i)

