
# Docstrings -
# Note: Docstrings are needed for future assignments
#

# # Lets look at PA06 conversion as an example
# #
# def f2c(fahrenheit):
#   """
#   convert an int or float temp in fahrenheit to a celsius float value
#   """
# 	celsius = (((fahrenheit - 32) * 5) / 9)
# 	return celsius



# # looking at the steps of troubleshooting
# #
# # Initial starting code: hangman_bug.py
#
# phrase = input("Enter a word or phrase: ").lower()
# data = '_'.join(phrase) + '_'
#
# wrong = 0
# while '_' in data and wrong < 6:
# 	print('Thing to guess:', data[1::2])
# 	letter = input('What letter? ').lower()
# 	while len(letter) != 1:
# 		letter = input('What letter? ')
# 	odata = data
# 	data.replace(letter + '_', letter + letter)
# 	if odata == data:
# 		wrong += 1
# 		print('Sorry, there was no', letter, 'in the phrase')
# 	else:
# 		print('Good guess!')
# 	run += 1
#
# if '_' in data:
# 	print('You lose; it was', phrase)
# else:
# 	print('You won in', run, 'steps! The answer was', phrase)



# # Hangman code after troubleshooting steps
# #
# # starting code: hangman_bug.py
#
# phrase = input("Enter a word or phrase: ").lower()
# data = '_'.join(phrase) + '_'
#
# run = 0
# wrong = 0
# #print("Good Location 2:", [phrase, data, run, wrong])
# while '_' in data and wrong < 6:
#    print('Thing to guess:', data[1::2])
#    letter = input('What letter? ').lower()
#    while len(letter) != 1:
#        letter = input('What letter? ')
#    #print("Unknown Location 3:", [phrase, data, run, wrong, letter])
#    odata = data
#    data = data.replace(letter + '_', letter + letter)
#    print("Unknown Location 4:", [phrase, data, run, wrong, letter, odata])
#    if odata == data:
#        print("Unknown Location 5:", [phrase, data, run, wrong, letter, odata])
#        wrong += 1
#        print("BAD Location 1:", [phrase, data, run, wrong, letter, odata])
#        print('Sorry, there was no', letter, 'in the phrase')
#    else:
#        print('Good guess!')
#    run += 1  # run = run + 1
#
# if '_' in data:
#    print('You lose; it was', phrase)
# else:
#    print('You won in', run, 'steps! The answer was', phrase)
#






