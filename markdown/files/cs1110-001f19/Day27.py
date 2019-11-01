# # Example reading and storing text. This should help in getting
# # ready to read in data from files.
# 
# # The text of a file might look like this:
# # ID,Type,Name
# # 3761,Elephant,Big Al
# # 9345,Lion,Lilly
# 
# # If we read that in as a single string and saved it in a variable,
# # the string would look like this:
# zoo_text = 'ID,Type,Name\n3761,Elephant,Ellie\n9345,Lion,Leo\n'
# print(zoo_text)
# 
# # Now let's divide this string into separate lines, after removing
# # unwanted whitespace at the beginning and end of the string
# line_list = zoo_text.strip().split('\n')
# print(line_list)
# 
# # Now let's divide each line into it's individual pieces
# # We'll store these in a new list
# details = []
# for each in line_list:
# 	current_line = each.split(',')
# 	details.append(current_line)
# print(details)
# print('')
# 
# # Now we can pull any information out of this list that we want
# # Let's create a variable to pick a single field that we want
# for field_num in range(len(details[0])):
# 	print('Here is the ' + details[0][field_num] + ' for each record:')
# 	for i in range(1, len(details)):
# 		print(details[i][field_num])
# 	print('')
# 
# print('Program finished')



# # Let's read from a real file
# # We found this one while surfing
# # the web during class - 'ncaa_colors.csv'
#
# # We usually store the name of the file in a variable
# file_name = 'ncaa_colors.csv'
#
# # The open() function returns a file object, we need that
# # to read from a file or write to a file
# f = open(file_name, 'r')
#
# # A file object's read() method reads the entire contents of a
# # file and returns it as a single string
# s = f.read()
#
# # # this is one way to read text from a file, one line at a time
# # for line in f:
# #
#
# # create a new list to store all of the data in
# teams = []
#
# # take the large string that contains the entire file,
# # and break it in to lines, one string per line
# s_list = s.strip().split('\n')
#
# # go through each string (row) and split it into individual fields
# for row in s_list:
#    row_list = row.strip().split(',')
#    teams.append(row_list)
#
# # Teams should now be a 2-dimensional list containing all the
# # data from the file. If should follow this pattern:
# # teams = [[row1--word1, row1--word2, row1--word3, ... ],
# #          [row2--word1, row2--word2, row2--word3, ... ], ... ]
#
#
# # iterate through the list by index value
# for i in range(0,len(teams)):
#    row = teams[i]  # store all data for the current row/line
#    color = row[2]  # color is the third field on each row/line
#    if 'blue' in color.lower() and 'orange' in color.lower():
#        print(teams[i][0], ' --- ', color)
