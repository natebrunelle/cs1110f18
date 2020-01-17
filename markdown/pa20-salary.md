---
title: "PA 20: salary.py"
...

# Background

A lot of information is freely available on the web, but not a lot of it is in forms that computers find useful to read.
A common use of regular expressions is to understand or **parse** data from a human-centric view like a webpage into a computer-centric view like CSV.

One source of data is [the Richmond Times-Dispatch's summary of Virginia state salaries](http://data.richmond.com/salaries/)'s, obtained using the state's [Freedom of Information statute](http://foiacouncil.dls.virginia.gov/).
To avoid overloading the newpaper's website with hundreds students testing their code, we have a mirror of the 2018--2019 UVA salary data you can have your code access on our servers for this assignment.

> <http://cs1110.cs.virginia.edu/files/uva2018/>

When you visit a page, you see a rendering of the content, but under the hood most web pages are written in a language called HTML.
Like Python, this is a text-based representation that describes what the computer is supposed to do.
Unlike Python, it is a *markup language*, not a *programming language*, meaning it is interested primarily in describing data rather than specifying processes.
The nuances of HTML are not important for our task; all you need to do is write regular expressions to find specific information within it.

You can view the HTML of any web page using the "view source" option of your web browser (typically either via the keyboard shortcut Ctrl+U or Cmd+Opt+U).
The source is what `urllib.request` will retrieve, what your regular expressions will need to look at, and what we discuss below.

# Task

The following writeup describes elements of the task you are to do, mostly with examples taken from the "view source" of [Jim Ryan's page](https://cs1110.cs.virginia.edu/files/uva2018/james-e-ryan).
Your job is to generalize the pattern and put it in a regular expression.
Some information has multiple locations; you only need to find one of the options.

## Name normalization

The URLs use full names, family name last, lower-case, with hyphens between name parts and no other punctuation.

If given                        Create
-----------------------------   ------------------------------
`James E. Ryan`                 `james-e-ryan`
`Ryan, James E`                 `james-e-ryan`
`james-e-ryan`                  `james-e-ryan`
`161048349`                     `161048349`
`Slaughter-Scott, Jacqueline`   `jacqueline-slaughter-scott`

Tip: Regexes are not required here.

## Find job title

Job title, e.g. the `President University of Virginia`, which can be found in multiple locations in the website:

    <meta property="og:description" content="Job title: President University of Virginia<br /> 2018 total gross pay: $750,000" />

and

    <span class="small text-muted" id="personjob">President University of Virginia</span>

(the `<title>` line also has a job title, but with the wrong case; use one of the two above)

You'll need a regular expression that (a) finds one of those lines and (b) has a group (parentheses) around the portion that is the job title (`President University of Virginia`).

After you get the group, if the job title contains `&amp;`, replace it with just `&`; likewise replace `&#39;` with `'`. For example, employee `181009456` has the listed job title `Store &amp; Warehouse Spec III` which should be presented as just `Store & Warehouse Spec III`; `181016364` is another good employee to test.



## Find total compensation

Total compensation appears in multiple locations:

    <meta property="og:description" content="Job title: President University of Virginia<br /> 2018 total gross pay: $750,000" />

and
    
    <h2 class="pay" id="paytotal">$750,000</h2>

and
    
    <div style="margin:0; float:left; background:#337ab7; height:100%; width:<%= getPct(paytype.amount, 750000) %>%;"></div>
     
Make a regular expression that finds one of these lines and has a group for the salary, and convert it to a `float` (`750000.0`{.python} in this case).


## Find rank, if given

Some (but not all) pages have a pay rank compared to other UVA employees; for example, the `1` in

    <tr><td>University of Virginia rank</td><td>1 of 8,582<!--not null --></td></tr>

If it is present, you'll want to turn it into an `int`{.python}.
If not, use the dummy-rank of `0`.
    

## Combine into a function

Write a function named `report` in a file `salary.py` that takes a name and returns three values:

-   The job title of that person.
-   That person's total salary.
-   That person's salary rank within UVA, or 0 if not provided.

If the person is not in the salary site, return `None, 0, 0`{.python}

## Style matters

In addition to functional correctness, some points will be reserved for

1.  having good variable names
1.  having meaningful docstrings for all functions you write


# Example Runs

If you run `salary.py` it should not do anything.
It defines functions, it does not run them.

If in a separate file you write

````
import salary

for name in (
        'James E. Ryan', 
        'Ryan, James E', 
        '181067633', 
        'Hao Ran Laurenc Lin', 
        '181016364',
        'Thomas Jefferson'
        ):
    job, money, rank = salary.report(name)
    print(name, 'is a', job, 'and makes', money, '(rank', str(rank)+')')
````

You should see

````
James E. Ryan is a President University of Virginia and makes 750000.0 (rank 1)
Ryan, James E is a President University of Virginia and makes 750000.0 (rank 1)
181067633 is a Hsekeep &/or Apparel Worker I and makes 23120.0 (rank 0)
Hao Ran Laurenc Lin is a Research Associate and makes 56600.0 (rank 5253)
181016364 is a WS Head Coach, Women's Basketb and makes 46000.0 (rank 0)
Thomas Jefferson is a None and makes 0 (rank 0)
````

# Thought Question

The site also gives a salary breakdown for each employee.
For some this is just their base salary:

    var pay = [ {'name': 'Base salary', 'amount': 33000 } ];

but for others it is more complicated:

    var pay = [ {'name': 'Base salary', 'amount': 188749 }, {'name': 'Additional compensation', 'amount': 15000 }, {'name': 'Non-state salary', 'amount': 371081 }, {'name': 'Deferred compensation', 'amount': 180000 } ];

Note that the above is not Python code; it is part of the webpage (a portion written in a language called JavaScript).

Try making a second function `breakdown` that returns a `dict` based on this salary breakdown, returning something like

````python
{'Base salary': 188749.0, 'Additional compensation': 15000.0, 'Non-state salary': 371081.0, 'Deferred compensation': 180000.0}
````
As a hint, try looking for all generic `'name': '...', 'ammount': ...` strings and adding each one to an initially-empty `dict`.

# Troubleshooting

There are a lot of things going on in this function.
Good coding practice would be to make a few extra functions to help out;
for example it might make sense to have a `name_to_URL(name)` function, etc.

Incidentally, the `name_to_url` proceess does not need regular expressions; it is enough to 

1.  remove periods
1.  find a comma (using `in`{.python}) and reorder the text if there is one (move what was before the comma to be after it)
2.  make it lower-case
3.  change spaces to hyphens

The easiest way to tell if the URL does not exist is to open it in a `try:`{.python} and handle failure in an `except:`{.python}

Since the values are identifiable by their surrounding context, try making regular expressions that match that context and keep the answer in a group, such as `<td>([0-9]+) of` for finding rank (which does not quite work as written...).

When `search` fails to find something, it returns `None`{.python}.

For most of the elements of the answer, `search` is the regular expression method you're most likely to want.
However, the compensation breakdown will probably benefit from a `finditer`, with a regular expression that matches the key in one group and the value in another group.

Make sure you are returning the right datatypes:

-   title is a `str`{.python}, or the value `None`{.python} (not `"None"`{.python})
-   income is a `float`{.python}
-   rank is an `int`{.python}

