# EXAMPLE START CODE

# # sample starting code to show exceptions
# def tickets(price, friends, savings):
#  total = friends * price
#  if total <= savings:
#     print('You can buy', friends,
#          'tickets at face value, it will cost', total, 'dollars.')
#  else:
#     print('Try to find tickets for', savings/friends, 'dollars.')
#
#
# a = input('What is the regular ticket price? ')
# b = input('How many friends do you have? ')
# c = input('How much do you have in savings? ')
# tickets(a,b,c)



# # example of handling different types of exceptions
# import urllib.request
#
# url = input("give me a url: ")
# try:
#     urllib.request.urlopen(url)
#     print('that was a valid url')
# except urllib.error.URLError:
#     print('that was not an active url')
# except ValueError:
#     print("that didn't even look like a url!")
# except:
#     print("I don't know, something bad happened")
# finally:
#     print("this is always printed")



# # example - an exception could be raised in multiple places
# def is_even(n):
#  #try:
#     return n % 2 == 0
#  #except:
#  #  return False
#
# def isnt_even(n):
#  return not is_even(n)
#
# def maybe_prime(n):
#  return n == 2 or isnt_even(n)
#
# test_inputs = [2,3,4,5,6]
# for each in test_inputs:
#  print(each, maybe_prime(each))


