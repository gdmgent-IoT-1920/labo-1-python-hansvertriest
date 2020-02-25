import random

secret_nr = random.randrange(1000,9999)

def validate_nr(correct_nr, nr):
	correct_nr_str = str(correct_nr)
	nr_str = str(nr)
	kippen = 0
	eieren = 0
	for index, char in enumerate(correct_nr_str):
		if char == nr_str[index]:
			kippen += 1
	found_characters = str(secret_nr)
	for index, char in enumerate(correct_nr_str):
		if char in nr_str and char in found_characters:
			eieren += 1
			found_characters = found_characters[:index] + found_characters[index+1:]
	eieren = eieren - kippen
	if eieren < 0 :
		eieren = 0
	return [kippen, eieren]

def printResult(result_array):
	if result_array[0] > 1 or result_array[0] == 0:
		if result_array[1] > 1 or result_array[1] == 0: 
			print(str(result_array[0]) + ' kippen en ' + str(result_array[1]) + ' eieren')
		else:
			print(str(result_array[0]) + ' kippen en ' + str(result_array[1]) + ' ei')
	else:
		if result_array[1] > 1 or result_array[1] == 0:
			print(str(result_array[0]) + ' kip en ' + str(result_array[1]) + ' eieren')
		else:
			print(str(result_array[0]) + ' kip en ' + str(result_array[1]) + ' ei')

nr_found = False
try_counter = 0

while not nr_found:
	usr_nr = input('Guess the number: ')
	print(usr_nr)
	try_counter += 1
	if secret_nr == usr_nr:
		print('You found the number in ' + str(try_counter) + ' times!')
	else:
		result = validate_nr(secret_nr, usr_nr)
		printResult(result)
	