
# # what if we wanted to run the following program multiple times?
# target = 77
# count = 10
# while count > 0:
#     z = int(input("Enter a number: "))
#     if z == target:
#         print("You win a prize!")
#     else:
#         print(str(count - 1), "left")
#     count -= 1
# print("Program finished")
# 
# # we could put this program inside of a loop




# tracing through a nested loop -
#
# def print_things(n):
# 	'''This functions will print ______ lines'''
# 	for i in range(n):
# 		for j in range(i):
# 			print('stuff', i, j)
#
# # How many lines are printed with the following function calls?
# print_things(0)
# print_things(1)
# print_things(2)
# print_things(3)
# print_things(4)
# print_things(5)
#
# print("program finished")



# another nested loop example
#
# def times_table(n):
# 	"""
# 	print the products of all integers between 0 and n as a table
# 	"""
# 	for row in range(n+1):
# 		print(str(row) + ": ", end="")
# 		for column in range(n):
# 			print(row * column, end='\t')
# 		print("")
#
# times_table(5)



# # code tracing with loops - 
# # what does this function do?
# def mystery(x, y):
# 	z = 0
# 	while x >= y:
# 		x -= y
# 		z += 1
# 	return z

# print(mystery(563,10))
# print(mystery(0,0)) # infinite loop!


# # more code tracing -
# # what does this function do?
# def mystery2(x, y):
# 	z = 0
# 	while x >= y:
# 		x = mystery(x,y)
# 		z += 1
# 	return z

#print(mystery2(563,10))









