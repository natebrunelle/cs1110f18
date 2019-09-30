---
title: "Lab 7: Hangman"
...


# Purpose of this lab

This lab has three goals

1.	Help them see the relationship between `if` and `while`.
2.	Help them develop a full program with limited scaffolding.
3.	Reinforce the idea of string methods and if statements.

If they finish, their `hangman_if.py` code will be quite long (hundreds of lines) and very repetitive.  This is correct.
This `hangman_while.py` code will be much shorter.

# Overview

Remind the students that

1.	They write two files; the first should *not* use loops
2.	The directions give hints
3.	PyCharm has a find-replace tool (demonstrate it for them) they are likely to find useful

# To get them started

First describe how the game of hangman works. After this show that each blank will have a letter labelling what belongs there. On a board we might put this label beneath the blank and hide it from the player. In the program, we just move that label to the left of the blank, and display only ever alternate character.

**Tell them "Try using a function before asking someone else what it does"**


# Example solution

I don't usually do this, but this code is so strange-looking I suspect many TAs will think the correct code looks wrong:
[my reference solution to this lab](https://kytos.cs.virginia.edu/cs1110/download.php?file=support/hangman_if.py).
