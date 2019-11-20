# Start with class roster example from Monday
# Just find userID's, but not if they're part of email addresses
# find ID's with middle initials
# just find students
# introduce anything - .  and  .*


# # Where we ended on Monday -
# # Sample text to search for userID's
# text = """
# User ID Email Address Role
#
# rp6zr    rp6zr@virginia.edu Instructor
# mst3k    mst3k@virginia.edu Student
# ab9cd    ab9cd@virginia.edu Student
# tj2a     tj2a@virginia.edu  Founder
#
# """
#
# import re
#
# compid_re = r"([a-z]{2,3})([2-9])[a-z]{1,3}"
#
# # build the thing the computer uses to search
# compid_finder = re.compile(compid_re)
#
# for match in compid_finder.finditer(text):
# 	initials = match.group(1)
# 	print(initials)



# $ only matches last location in text
# ^ only matches beginning location of text
# \b matches all word boundaries


# phone number example
# list many valid numbers
# list many invalid (but close to valid) numbers
# Official rules -
#   https://en.wikipedia.org/wiki/North_American_Numbering_Plan
# [2-9][0-9]{2}-([2-9][0-9]{2}-)?[0-9]{4}|\([2-9][0-9]{2}\) ?[2-9][0-9]{2}-[0-9]{4}
# [ ][2-9][0-9]{2}-([2-9][0-9]{2}-)?[0-9]{4}|\([2-9][0-9]{2}\) ?[2-9][0-9]{2}-[0-9]{4}
# Add the space at the beginning to avoid recognizing a number
# that starts with an invalid area code
#
# Breaking this up in to smaller pieces
#
# Writing by parts:
# [area code]?[office code][line number]
# area code = [2-9][0-9]{2}-|\([2-9][0-9]{2}\) ?
# office code = [2-9][0-9]{2}-
# line number = [0-9]{4}
#
# ([2-9][0-9]{2}-|\([2-9][0-9]{2}\) ?)?[2-9][0-9]{2}-[0-9]{4}
#
#

# import re
#
# text = '''The following are extracts from http://en.wikipedia.org
#
# For example, 234-235-5678 or (234) 235-5678 or (234)235-5678
# is a valid telephone number with area code 234,
# central office prefix (exchange) 235, and line number 5678.
# The number 234-911-5678 is invalid, because the central office code
# must not be in the form N11. 314-159-2653 is invalid, because the office code
# must not begin with 1. 123-234-5678 is invalid, because the NPA must not begin
# with 0 or 1.
#
# The country calling code for all countries participating in the NANP is 1.
# In international format, an NANP number should be listed as +1 301 555 0100,
# where 301 is an area code (Maryland).'''
#
# #phone = r'[2-9][0-9]{2}\-([2-9][0-9]{2}\-)?[0-9]{4}|\([2-9][0-9]{2}\) ?[2-9][0-9]{2}\-[0-9]{4}'
# area = r'(\([0-9]{3}\) ? | [0-9]{3}-)?'
# office = r'[0-9]{3}-'
# rest = r'[0-9]{4}'
# phone = area + office + rest
# #phone = r'(\([0-9]{3}\) ? | [0-9]{3}-)?[0-9]{3}-[0-9]{4}'
# phone_finder = re.compile(phone)
#
# for match in phone_finder.finditer(text):
#     print(match.group())
#
#
#
# text = '''
# These should be good:
# 555-1234
# 434-555-1234
# (434)555-1234
# (434) 555-1234
# These should not be recognized:
# 555-123
# 5551234
# 5555-1234
# 111-1234
# '''
import re

# [area code]?[office code][line number]
# area code = [2-9][0-9]{2}-|\([2-9][0-9]{2}\) ?
# office code = [2-9][0-9]{2}-
# line number = [0-9]{4}

# area_code = r"[2-9][0-9]{2}-|\([2-9][0-9]{2}\) ?"
# office_code = r"[2-9][0-9]{2}-"
# line_number = r"[0-9]{4}"
# phone_re = area_code + office_code + line_number
# phone_finder = re.compile(phone_re)
#
# for match in phone_finder.finditer(text):
# 	my_match = match.group()
# 	print(my_match)
#
#

