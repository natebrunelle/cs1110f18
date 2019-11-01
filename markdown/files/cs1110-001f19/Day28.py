# Here is some sample data for a local file, 'vastats.csv'
# Note: the file that exists at:
# 'http://cs1110.cs.virginia.edu/files/vastats.csv' is much larger
'''
Type,Name,Total Population,Male,Female
A,Virginia,7078515,3471895,3606620
A,Accomack County,38305,18590,19715
A,Albemarle County,79236,38002,41234
A,Alleghany County,12926,6450,6476
A,Amelia County,11400,5622,5778
'''



# Let's open a local csv file, and see 4 different ways that we can
# read in the data


# file_name = 'vastats.csv'

# print('\n---------------- read() ----------------' * 3)
#
# f=open(file_name, 'r')
# a = f.read()
# print(type(a))
# print(a)
# f.close()

# print('\n---------------- readline() ----------------' * 3)
# f=open(file_name, 'r')
# b = f.readline()
# print(type(b))
# print(b)
# f.close()

# print('\n---------------- readlines() ----------------' * 3)
# f=open(file_name, 'r')
# c = f.readlines()
# print(type(c), c)
# f.close()

# print('\n---------------- for <line> in <file>: ----------------' * 3)
# f=open(file_name, 'r')
# for line in f:
# 	print('\n-------- loop ----------')
# 	print(type(line))
# 	print(line)
# f.close()






# Now let's connect to a file that exists online
# We need to import a new library to open online files
#
# import urllib.request
# url = 'http://cs1110.cs.virginia.edu/files/vastats.csv'
# f = urllib.request.urlopen(url) # this is like open(), put for online


# print('\n---------------- read() ----------------' * 3)
#
# # decode() is needed since it's an online file in byte format
# a = f.read().decode('utf-8')
# print(type(a))
# print(a)
# f.close()
# #

# print('\n---------------- readline() ----------------' * 3)
# f = urllib.request.urlopen(url)
# b = f.readline().decode('utf-8')
# print(type(b))
# print(b)
# f.close()

# print('\n---------------- readlines() ----------------' * 3)
# f = urllib.request.urlopen(url)
# c = f.readlines()
# print(type(c),'of',type(c[0]))
# print(c)
# my_string = c[0].decode('utf-8')
# print(type(my_string),my_string)
# f.close()

# print('\n---------------- for <line> in <file>: ----------------' * 3)
# f = urllib.request.urlopen(url)
# for d in f:
# 	d = d.decode('utf-8')
# 	print('-------- loop ----------')
# 	print(type(d))
# 	print(d)
# f.close()


# f = urllib.request.urlopen(url)
# line_list = []
# for each in f:
# 	line = each.decode('utf-8').strip().split(',')
# 	line_list.append(line)
# # print(type(line_list),type(line_list[0]))  # debugging
# # print(line_list[0])  #debugging
# header = line_list[0]  # store the first line in a separate variable
# line_list.pop(0)  # then remove that first line because it's not a city
#
# # Find the cities with populations larger than 100,000
# for i in range(len(line_list)):
# 	city = line_list[i]
# 	if int(city[2]) > 100000:
# 		print(city[1], '........', city[2])
#
#
# f.close()



