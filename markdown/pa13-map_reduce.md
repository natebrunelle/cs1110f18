---
title: "PA 13: map_reduce.py"
...

# Task

Early in the days of "Big Data" the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) programming model became quite popular.
The core of this model is two functions, `map` and `reduce`, which you will write in this assignment.

Write a file named `map_reduce.py` that implements two functions:

## `mymap(func, lst)`{.python}

Given a single-argument function and a list, return a list containing the result of applying that function to each element of that list.
For example, `mymap(abs, [3,-1,4,-1,5,-9])`{.python} should return `[3, 1, 4, 1, 5, 9]`.

## `myreduce(func, lst)`{.python}

Given a two-argument function and a list, return the result of using the function repeatedly to combine all elements of the list into a single value.
For example, `myreduce(pow, [3,-1,4,1,-5])`{.python} should compute `pow(pow(pow(pow(3, -1), 4), 1), -5)`{.python} and return `3486784401.0`{.python}.

## Restrictions

There are several full or partial implemenations of map and reduce in Python already; since this is a programming exercise, you may not use them.
Do not import anything.
Do not use the built-in function `map`.
Do not use list comprehensions (you probably don't even know what those are, but if you do don't use them).

Neither of your functions (nor the file itself) should `print`{.python} anything nor ask for any `input`{.python}.

In addition to functional correctness, some points will be reserved for

1.  having good variable names
1.  having meaningful docstrings for all functions you write

# Example Invocations

When you run `map_reduce.py`, nothing should happen.
It defines a function, it does not run it.

If in another file (which you do not submit) you write the following:

````python
import map_reduce

def wiggle(a,b):
    a, b = abs(a), abs(b)
    if a > b:
        a,b = b,a
    c = b % a
    if c == 0:
        return a + b
    return c
def waggle(a):
    if a < 0:
        return -2*a
    else:
        return 2*a+1
x = [3, -1, 4, -1, 5, -9, 2, -6, 5, -3, 5]

print(map_reduce.myreduce(wiggle, x))
print(map_reduce.mymap(waggle, x))
print(map_reduce.myreduce(wiggle, map_reduce.mymap(waggle, x)))
print(x)
````

you should get the following output:

````
6
[7, 2, 9, 2, 11, 18, 5, 12, 11, 6, 11]
12
[3, -1, 4, -1, 5, -9, 2, -6, 5, -3, 5]
````

# Troubleshooting

Although our example invocation uses custom functions, it might be easier to test using the `abs` and `pow` examples in the function descriptions.

Particularly for `myreduce`, but likely also for `mymap`, you'll want to test smaller examples than we have first.
What's `myreduce(pow, [2,3])`, for example?
How about `myreduce(pow, [2,3,4])`?
