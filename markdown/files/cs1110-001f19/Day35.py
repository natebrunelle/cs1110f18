# Regular Expressions, 2nd Day

'''
1.) import re
2.) finder = re.compile(regex_rstring)
3.) use the finder
     finder.search(text):
        find the first place in the text that matches the regex
     finder.finditer(text)
        gives a collection of match objects
        one from each place in the text that matches the regex
     finder.findall(text)
        A list containing:
           0 parentheses: m.group()
           1 paren: m.group(1)
           2+ paren: m.groups()
4.) Use the match object
  group: The text we matched on
  start: the index of the start of the match
  end: the index of the end of the match
  groups
'''


# # Sample text to search for userID's
# text = """
# User ID Email Address Role
#
# rp6zr    rp6zr@virginia.edu Instructor
# mst3k    mst3k@virginia.edu Student
# ab9cd    ab9cd@virginia.edu Student
#
# """





# import re
#
# compid_re = r"([a-z]{2,3})([2-9])[a-z]{1,3}"
#
# # build the thing the computer uses to search
# compid_finder = re.compile(compid_re)

# match = compid_finder.search(text)
# print(match)
#
# start_index = match.start()
# end_index = match.end()
# initials = match.group(1)
# digit = match.group(2)
# print(start_index)
# print(end_index)
# print(initials)
# print(digit)


# for match in compid_finder.finditer(text):
#  initials = match.group(1)
#  print(initials)


