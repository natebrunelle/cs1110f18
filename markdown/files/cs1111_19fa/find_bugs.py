def get_index_of(string, letter):
    index = -1
    for i in range(1, len(string)):
        # check if we get the right character
        print(i, string[i])
        if string[i] == letter:
            index = i
            # check if the if-code-block is executed
            print(string[i], "=", letter, "i=", i)

    return index


# Test0: inputs of "python", "o"
print(get_index_of("python", "o"))  # expected: 4, actual: 4
# Test1: inputs “python”, “z”
print(get_index_of("python", "z"))  # expected: -1, actual: -1
# Test2: inputs “python”, “z”
print(get_index_of("python", "p"))  # expected: 0, actual: -1
# Test3: inputs “banana”, “a”
print(get_index_of("banana", "a"))  # expected: 1, actual: 5
