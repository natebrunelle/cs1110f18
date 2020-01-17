---
title: "PA Optional: readability.py (ungraded)"
...

# Task

Note: This assignment is meant for your own practice only. We will not grade it, there are no automated graders for the assignment.

Various metrics exist for assessing the reading level of text. One such metric is the Automated Readability Index. This metric determines the reading level using a mathematical operation over the number of words and the number of characters in the text. See the [wikipedia article](https://en.wikipedia.org/wiki/Automated_readability_index) for more information, and for the formula used to cacluate the metric.

For this assignment, write a file named `readability.py` that has a function `automated_index` which:

-   Receives the name of a local file as input
-   counts the number of words in the file
-   counts the number of characters in the file (excluding numbers and punctuation, so only includes letter a-z, either upper or lower case)
-   counts the number of sentences in the file (assume always separated by a period, exclamation point, or question mark, but not necessarily by a newline)
-   returns the Automated Readbility Index of the text in the file (as an `int`)




## Style matters

In addition to functional correctness, some points will be reserved for

1.  having good variable names
1.  having meaningful docstrings for all functions you write

# Example Invocations

When you run `readbility.py`, nothing should happen.
It defines a function, it does not run one.

We have provided a few example files for you:

-   The [instructions for Exam 2](/files/readability/examinstructions.txt)
-   The [course syllabus](/files/readability/syllabus.txt)
-   The entire text of Shakespeare's [Hamlet](/files/readability/hamlet.txt)
-   The entire text of [War and Peace](/files/readability/warandpeace.txt)
-   The entire text of [The Velveteen Rabbit](/files/readability/velveteenrabbit.txt)
-   [Rapunzel](/files/readability/rapunzel.txt) by the Brothers Grimm
-   The [intro for A Tale of Two Cities](/files/readability/totcintro.txt)
-   [Baa Baa Black Sheep](/files/readability/baabaa.txt)
-   Lyrics to [Heartless](/files/readability/heartless.txt) by Kanye West
-   [George Washington's Farewell Address](/files/readability/washington_farewell.txt)
-   [The Declaration of Independence](/files/readability/declaration.txt)

If you download each of the above files into your pycharm project folder, then in another file (which you do not submit) you write the following:

````python
import readbility

print('exam', readbility.automated_index('examinstructions.txt'))
print('syllabus', readbility.automated_index('syllabus.txt'))
print('hamlet', readbility.automated_index('hamlet.txt'))
print('warandpeace', readbility.automated_index('warandpeace.txt'))
print('velveteen', readbility.automated_index('velveteenrabbit.txt'))
print('rapunzel', readbility.automated_index('rapunzel.txt'))
print('TOTC', readbility.automated_index('totcintro.txt'))
print('baa baa', readbility.automated_index('baabaa.txt'))
print('heartless', readbility.automated_index('heartless.txt'))
print('Washington Farewell', readbility.automated_index('washington_farewell.txt'))
print('Declaration of Independence', readbility.automated_index('declaration.txt'))
````

you should get the following output:

````
exam 4
syllabus 8
hamlet 5
warandpeace 6
velveteen 4
rapunzel 8
TOTC 56
baa baa 3
heartless 0
Washington Farewell 17
Declaration of Independence 18

````

# Troubleshooting

To make sure you're only getting letters of the alphabet in your word count, you want to make sure you only count characters that appear in the following string (after they've been made lowercase): `'abcdefghijklmnopqrstuvwxyz'`
