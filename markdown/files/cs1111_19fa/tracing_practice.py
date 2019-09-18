# 1. What does the following math_trick code print? Trace through the code by hand.
#    Check your answer by running the code.

def func(a, b):
    if a > b:
        return "bigger"
    else:
        return "not bigger"


#MAIN
x = 2
y = 3
print("Question 1")
print(func(y, x))
print(func(x, y))
y = func(x, x)
print(y)

############################################

# 2. What does the following math_trick code print? Trace through the code by hand.
#    Check your answer by running the code.

def func(x, y):
    x = 3
    y = [1]
    return x


x = 2
y = [3]
print("Question 2")
print(func(x, y))
print(x)
print(y)

############################################

# 3. What does the following math_trick code print? Trace through the code by hand.
#    Check your answer by running the code.

def func(x, y, a, b):
    x = y
    y = 1
    return a - 2


x = 2
y = 3
y = func(x, y, x, y)
print("Question 3")
print(x)
print(y)

############################################

# 4. What does the following math_trick code print? Trace through the code by hand.
#    Check your answer by running the code.


def func4(a, y):
    a[0] = 2
    y[1] = 7
    y = [4]
    return y


x = [3, 4]
y = [x, 4, 5]
func4(x, y)
print("Question 4")
print(x)
print(y)

############################################

# 5. What does the following math_trick code print? Trace through the code by hand.
#    Check your answer by running the code.

def func2(a, z):
    a = 3
    z.append(a)


def func1(a, y):
    a = 2
    y[1] = 1
    y = [4]
    func2(a, y)
    print(a)
    print(y)
    return "hello"


x = 7
y = [x, 4, 5]
func1(x, y)
print("Question 5")
print(x)
print(y)
