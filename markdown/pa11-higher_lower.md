---
title: "PA 11: higher_lower.py"
...

# Task

Write a file named `higher_lower.py` that plays a simple guessing game with the user. 



The number to guess is either selected by the user or a randomly generated number between 1 and 100. The number of guesses is chosen by the user. On each turn, the program accepts one guess from the user. If the user guesses right, it will say “You win!”. If the user’s guess is higher or lower than the correct answer, the program will say “The number is higher than that.” (or “The number is lower than that.”).  If after the given number of guesses the user still hasn’t guessed right, print “You lose; the number was x.”, where x is the answer (the number the user was to guess).



Before the game begins,

1. Ask what number to pick. If they say “−1”, pick randomly; otherwise, use their number even if it is outside the 1–100 range.
2. Ask how many guesses they should have. You may assume they respond with a positive integer.


In addition to functional correctness, some points will be reserved for

1. having good variable names
2. having meaningful docstrings for any functions you write (note: functions are not required for this assignment, but might make sense).


# Example Invocations

An example run of the program might look like:

````
What should the answer be? `19`
How many guesses? `9`
Guess a number: `9`
The number is higher than that.
Guess a number: `40`
The number is lower than that.
Guess a number: `19`
You win!
````

Another run might look like:

````
What should the answer be? `-1`
How many guesses? `5`
Guess a number: `5`
The number is higher than that.
Guess a number: `100`
The number is lower than that.
Guess a number: `50`
The number is lower than that.
Guess a number: `25`
The number is lower than that.
Guess a number: `12`
You lose; the number was 7.
````

(note: because the number is picked randomly, each `-1` game will be different)

# Thought Question

Try adding a loop to ensure that the number of guesses is a positive number (or -1), asking again if it isn't.


# Troubleshooting

To get a random integer

````python
import random

# set low and high here

num = random.randrange(low, high)

if low <= num < high:
    print('This is always true because this is how randrange works')
else:
    print('This line never prints because it is not how randrange works')
````

Note that the math is $low ≤ num < high$ not $low ≤ num ≤ high$.
To randomly get one of {3, 4, 5} you'd need to write `random.randrange(3, 6)`{.python}.


---

Every prompt of every `input`{.python} should end with a space character, for this and every other assignment that uses `input`{.python}. 

---

You'll want to use a loop.  Both `for`{.python} and `while`{.python} can work.

---

You'll need to keep going as long as both (a) the number of guesses is has not reached the maximum and (b) the correct guess has not been made.

-   One approach: use an `and`{.python} in the `while`{.python} condition expression.

-   One approach: have the loop repeat a fixed number of times (probably using `for`), and use a `break`{.python} inside it to exit early if they guess correctly.

----

There are four possible responses to a guess

-   Win
-   Lose
-   Higher
-   Lower

After each guess only one of the four should be displayed.
