---
title: Python functions and methods you should know
...

This document attempts to list the built-in functions, methods, and types that we expect every student will know well enough to ask about on exams.

All three exams are listed, using notes from previous semesters, but only the next one has been reviewed for accuracy based on topical adjustments for this semester.


# Exam 1

-   [cover page for exam1 for Spring 19](files/s19e1cover.pdf)
-   [how to fill in TPEGS footers](lab05-paper.html#TPEGS)
-   `str(value)`{.python}
-   `int(value)`{.python}
-   `float(value)`{.python}
-   `print(things, to, be, displayed)`{.python}
-   `input(prompt)`{.python}
-   `type(value)`{.python}
-   various operators (like `**`{.python} and `and`{.python}) and control constructs (like `if`{.python} and `def`{.python})
-   [other exam 1 topics](lab05-paper.html#things-we-expect-you-to-know)

Notably, `turtle` is not on the above list.

See also the previous exams:

Semester    | Exam                       | Key/Rubric
------------|----------------------------|-----------------------------------
Spring 2017 | [s2017e1.pdf](files/s2017e1.pdf) | [s2017e1key.txt](files/s2017e1key.txt)
Fall 2017   | [f2017e1.pdf](files/f2017e1.pdf) | [f2017e1key.html](files/f2017e1key.html)
Spring 2018   | [s2018e1.pdf](files/s2018e1.pdf) | [s2018e1key.html](files/s2018e1key.html)
Fall 2018   | [f2018e1.pdf](files/f2018e1.pdf) | [f2018e1key.html](https://docs.google.com/presentation/d/1stl9TeDPJA0MEVhsdMp_8C9Y6bvTuGKLHOg_V_w0eTA/edit#slide=id.g43d6d2d9d2_0_0)
Spring 2019 | [s2019e1.pdf](files/s2019e1.pdf) | [s2019e1key.pdf](files/s2019e1key.pdf) 

# Exam 2

Since exam 1, we have covered

-   Boolean values (`True`{.python} and `False`{.python}) and operators (`and`{.python}, `or`{.python},  and `not`{.python})
-   Test case selection and debugging strategies
-   Loops (`while`{.python}, `for`{.python})
-   Loops inside of loops (nested loops)
-   Collection types (`str`{.python}, `list`{.python}, `tuple`{.python}, `range`{.python})
-   Lists with lists as elements (e.g. 2d lists)
-   The basics of the `dict`{.python} datatype
-   Reading files
-   Reading tabular data (such as CSV)

While exam 2 is not designed to be an cumulative exam (i.e., we won't ask questions we could have asked for exam 1), the new material builds off old material so cumulative understanding is expected.

In general, we find questions directly about `tuple`{.python}, test case selection, and debugging strategies do not fit well into our exams.  However, the underlying concepts may appear in some way.  We typically intentionally test all other topics.

We expect you to know the following built-in and library functions, in addition to those listed under exam 1:

-   `import random`{.python}
    -   `random.randrange(lo, hi)`{.python}
-   `str`{.python}
    -   `substring in string`{.python}
    -   `string1 + string2`{.python}
    -   `string.strip()`{.python}
    -   `string.split()`{.python}
    -   `string.split(delimiter)`{.python}
    -   `string.find(substring)`{.python}
-   `list`{.python}
    -   `element in lst`{.python}
    -   `lst.append(value)`{.python}
    -   `lst.insert(index, value)`{.python}
    -   `lst.remove(value)`{.python}
    -   `lst.pop(index)`{.python}
    -   `lst.sort()`{.python}
    -   `lst.index(element)`{.python}
    -   `lst[start:end]`{.python}
-   `list(collection)`{.python}
-   `range(end)`{.python}
-   `range(start, end)`{.python}
-   `range(start, end, step)`{.python}
-   `dict`{.python}
    -   `mapping.keys()`{.python}
    -   `mapping.values()`{.python}
    -   `mapping.items()`{.python}
    -   `mapping.pop(key)`{.python}
-   `open(filename)`
    -   `connection.read()`{.python}
    -   `connection.readline()`{.python}
    -   some way of iterating lines (`connection.readlines()`{.python}, or `connection.read().split('\n')`{.python}, or `for line in connection`{.python})

See also the previous exams:

Semester    | Exam                       | Key/Rubric
------------|----------------------------|-----------------------------------
Spring 2017 | [s2017e2.pdf](files/s2017e2.pdf) | [s2017e2key.txt](files/s2017e2key.txt)
Fall 2017   | [f2017e2.pdf](files/f2017e2.pdf) | [f2017e2key.html](files/f2017e2key.html)
Spring 2018 | [s2018e2.pdf](files/s2018e2.pdf) | [s2018e2key.html](files/s2018e2key.html)
Fall 2018 | [f2018e2.pdf](files/f2018e2.pdf) | [f2018e2key.html](https://docs.google.com/presentation/d/1uGC0W5efFVIoSMu3DRr1qYHqMmDclfLajw_tlQdryIw)
Spring 2019 | [s2019e2.pdf](files/s2019e2.pdf) | [s2019e2key.pdf](files/s2019e2key.pdf) 


# Exam 3

-   everything listed for exams 1 and 2 (exam 3 is cumulative, including questions intentionally testing previous exam topics, though it does not include `turtle`)
-   `try:`{.python}/`except:`{.python}
-   `import pygame, gamebox`{.python}
    -   `box1.touches(box2)`{.python}
    -   `box1.move_to_stop_overlapping(box2)`{.python}
    -   `box1.speedx`{.python}, `box1.speedy`{.python}, and `box1.move_speed()`{.python}
    -   `camera.draw(box)`{.python}
    -   `camera.display()`{.python}
    -   `timer_loop(ticks_per_second, ticks)`{.python} and the basics of how to write a `ticks` function, including
        -   `ticks`'s argument is a collection of the keys being pressed
        -   `ticks` is invoked by gamebox `ticks_per_second` times every second
    -   We won't require you to remember the name of any of the `pygame` or `gamebox` functions,
        but you will need to know how to use them and what they do 
-   `import re`{.python}
    -   `re.compile(r'...')`{.python}, including the use of `.`, `[]`, `()`, `+`, `*`, and `?`
    -   `compiled_re.search(text)`{.python}
    -   `compiled_re.finditer(text)`{.python}
    -   `match.group()`{.python}
    -   `match.group(n)`{.python}
    -   `match.groups()`{.python}
-   `open(filename, 'w')`{.python}
-   `with open(...) as f:`{.python}
-   `print(..., file=f)`{.python}
-   `urllib.request`{.python}, (i.e. reading from the web)

See also the previous exams:

Semester    | Exam                       | Key/Rubric
------------|----------------------------|-----------------------------------
Spring 2016 non-coding Qs | (not available) | [CS111X-S16-Final-KEY.pdf](files/CS111X-S16-Final-KEY.pdf)
Spring 2016 Coding Q | [CS111X-S16-Final-Coding.pdf](files/CS111X-S16-Final-Coding.pdf) | (not available)
Fall 2016   | [CS111X-F16-Final.pdf](files/CS111X-F16-Final.pdf) | [CS111X-F16-Final-KEY.pdf](files/CS111X-F16-Final-KEY.pdf)
Spring 2017 | [s2017e3.pdf](files/s2017e3.pdf) | [s2017e3key.txt](files/s2017e3key.txt)
Fall 2017 | [f2017e3.pdf](files/f2017e3.pdf) | [f2017e3key.html](files/f2017e3key.html)
Spring 2018 | [s2018e3.pdf](files/s2018e3.pdf) | [s2018e3key.html](files/s2018e3key.html)
Fall 2018 | [f2018e3.pdf](files/f2018e3.pdf) | [f2018e3key.html](https://docs.google.com/document/d/1aaUiHwW00c46sk-7-69X6BuppJ_jKydAUZxp4VbBVjA/edit#heading=h.z0wg0h5of4gh)
Spring 2019 | [s2019e3.pdf](files/s2019e3.pdf) | [s2019e3key.pdf](files/s2019e3key.pdf) 

Final exams tend to change from one semester to another more than do other exams, so older exams are not necessarily the best indicator of future exams.
