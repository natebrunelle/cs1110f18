print("Hello world")

#--------------------------#

# function = reusable unit of code that performs a specific task

# built-in functions: python provides many built-in functions that do common tasks

# When you call a function, you code the name of the function followed by a pair of parentheses.
# Within the parentheses, you code any arguments that the function requires,
# separate multiple arguments with commas.

# Syntax for calling function
# function_name([arguments])

# print([data]) function
# Prints the data argument to the console followed by a new line character
# If the call doesn't include data argument, this function prints a blank line to the console

print("Hello")
print()
print("Goodbye!")

#--------------------------#

# Here is how to comment (start with #)
# Guidelines for using comments:
# - use comments to describe portions of code tha are hard to understand, but don't overdo them
# - use comments to comment out (or disable) statements that you don't want to execute
# - if you change the code that's described by comments, change the comment too

# To comment a block of lines
# - select all the lines to be commented
# - For Mac: press a "command" key and /
# - For Window: press a "control" key and /

#--------------------------#

# an indentation error
#  print("indentation error")
# notice the red wiggly line

#--------------------------#

# two ways to continue one statement over two or more lines
# 1. Implicit continuation: divide statements after parentheses, brackets, and braces
#    and before or after a plus operator
print("My name is Will" + " and my favorite courses are " +
      "\nCS 1111" +
      "\nCS 2110" +
      " and \nCS 2501 SDE")

# 2. Explicit continuation: use the \ character to divide statements anywhere on a line
t = "My name is Will" + " and my favorite courses are " \
      + "\nCS 1111" \
      + "\nCS 4640" \
      + " and \nCS 2501 SDE"
print(t)

# \n is a new line character --> force new line
# + sign concatenates strings (when using with numbers, + sign does an arithmetic operation)

#--------------------------#

# working with quotations and output format
print("My favorite courses are : " + "'CS 1111'")        # use different quatations
print("My favorite courses are : " + "\'CS 1111\'")      # use an escape character
print("My favorite courses are : " + "\"CS 1111\"")      # use an escape character

#--------------------------#

# Value of a variable can change as code executes
# A data type defines the type of data for a value
# An assignment statement uses the equals sign (=) to assign a value to a variable.
# The value can be a literal value, another variable, or an expression like the arithmetic expressions.

# In Python, you can assign a value of any data type to a variable,
# even if that variable has previously been assigned to a value of a different data type.
# This is referred to as "dynamic typing"

# Because variable names are case-sensitive,
# be sure to use the correct case when coding the names of variables.

#--------------------------#

# Initialize variables and assigns data (value) to them
product_name = "table"      # set product_name to a str of "table"
quantity1 = 3               # set quantity1 to an int value of 3
quantity2 = 5               # set quantity2 to an int value of 5
list_price = 19.99          # set list_price to a float value of 19.99
list_price = 19.99 + 10     # set list_price to a value of an expression 19.99 + 10
print(list_price)           # let's see what it looks like

# assigns new data to the variables above
product_name = "chair"      # set product_name to a str of "chair"
quantity1 = 10              # set quantity1 to an int value of 10
quantity1 = quantity2       # set quantity1 to an int value of 5
quantity1 = "15"            # set list_price to a str value of "15", not an int of 15

# error cause by incorrect an undefined variable
# quantity1 = Quantity2       # NameError: 'Quantity2' is not defined
# reminder: variable name is case sensitive

r = 5  # Create variable r
y = R  # Error because R is not a variable, but r is
y = r  # Valid

#--------------------------#

# Rules for naming variables
# - begin with a letter or underscore
# - can't contain spaces, punctuation, or special characters other than underscore
# - can't begin with a number, but can use numbers later in the name
# - can't be the same as a keyword that's reserved by Python
# - naming styles:
#   -- underscore notation: variable_name
#   -- camel case: variableName     (not prefer by Python programmers, not recommend)

# What we, CS 111x, consider as good variable names
# - start with lowercase letter
# - use underscore notation
# - use meaningful names that are easy to remember
# - when possible, should be at least 2 characters long
# - Don't use the names of built-in functions (such as print()) or modules (such as turtle or random)

#--------------------------#

# Here are some Python keywords
#  and      as      assert      break       class       continue
#  def      del     elif        else        except      False
#  finally  for     from        global      if          import
#  in       is      lambda      None        not         or
#  pass     raise   return      True        try         while
#  with     yield



# https://storage.googleapis.com/cs1111/examples/transition-to-code.py