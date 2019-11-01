---
title: "PA 15b: readability.py (ungraded)"
...

# Task

Various metrics exist for assessing the reading level of writing. One such metric is the Automated Readability Index. This metric determines the reading level using an mathematical operation over the number of words and the number of characters in the text. See the [wikipedia article](https://en.wikipedia.org/wiki/Automated_readability_index) for more information, and for the formula used to cacluate the metric.

For this assignment, write a file names `readability.py` that has a function `automated_index` which:

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
-   The entire text of [The Velveteen Rabbit]((/files/readability/velveteenrabbit.txt)
-   [Rapunzel](/files/readability/rapunzel.txt) by the Brothers Grimm
-   The [intro for A Tale of Two Cities](/files/readability/totci.txt)
-   [Baa Baa Black Sheep](/files/readability/baabaa.txt)
-   Lyrics to [Heartless](/files/readability/heartless.txt) by Kanye West

If you download each of the above files into your pycharm project folder, then in another file (which you do not submit) you write the following:

````python
import readbility

print(readbility.automated_index('examinstructions.txt'))
print(readbility.automated_index('syllabus.txt'))
print(readbility.automated_index('hamlet.txt'))
print(readbility.automated_index('warandpeace.txt'))
print(readbility.automated_index('velveteenrabbit.txt'))
print(readbility.automated_index('rapunzel.txt'))
print(readbility.automated_index('totcintro.txt'))
print(readbility.automated_index('baabaa.txt'))
print(readbility.automated_index('heartless.txt'))
````

you should get the following output:

````
4
8
5
6
4
8
55
3
0
````

# Troubleshooting

To make sure you're only getting letters of the alphabet in your word count, you want to make sure you only count characters that appear in the following string (after they've been made lowercase): `'abcdefghijklmnopqrstuvwxyz'`
