# Practice 1


def replace(word, to_replace):
    out = ""
    for letter in word:
        if letter == to_replace:
            out += "*"
        else:
            out += letter
    return out


print("=====Practice 1 tests=====")
print(replace("bird", "c"))            # bird
print(replace("bird", "i"))            # b*rd
print(replace("badapple", "a"))        # b*d*pple
print(replace("bidipple", "i"))        # b*d*pple

# Practice 2


def count_sum(lst):
    num = 0;
    for i in range(len(lst) - 1):
        if lst[i] + lst[i+1] == 10:
            num += 1
    return num


print("=====Practice 2 tests=====")
print(count_sum([]))                                  # 0
print(count_sum([1]))                                 # 0
print(count_sum([5, 5]))                              # 1
print(count_sum([5, 5, 6, 4, 8]))                     # 2
print(count_sum([2, 7, 3, 1, 9, 5, 5, 4, 6, 8]))      # 4

# Practice 3


def count_occurrence(word, substr):
    num = 0;
    for i in range(len(word)):
        if word[i: (i+len(substr)) ] == substr:
            num += 1;
    return num


print("=====Practice 3 tests=====")
print(count_occurrence("mississippi", "i"))           #  4
print(count_occurrence("mississippi", "is"))          #  2
print(count_occurrence("mississippi", "sis"))         #  1
print(count_occurrence("mississippi", "a"))           #  0
print(count_occurrence("mississippi", "sit"))         #  0
