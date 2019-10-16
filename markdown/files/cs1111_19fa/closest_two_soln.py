def closest_two(lst):
    first_number = lst[0]
    second_number = lst[1]
    minimum_diff = abs(lst[0] - lst[1])
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if i == j:
                continue
            current_diff = abs(lst[i] - lst[j])
            if current_diff < minimum_diff:
                first_number = lst[i]
                second_number = lst[j]
                minimum_diff = current_diff
    return [first_number, second_number]


print(closest_two([8, 4, 6, -1, 3, 10, -4]))