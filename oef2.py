file = open("namen.txt", "r")

lines = file.readlines()

filtered_lines = []

for name in lines:
	filtered_lines.append(name.replace('\n',''))

def get_dict(array):
	dictionary = {}
	for name in array:
		occurences = array.count(name)
		dictionary[name] = occurences
	return dictionary

def show_dict(dictionary):
	for key in dictionary:
		print(key + ': ' + str(dictionary[key]))


show_dict(get_dict(filtered_lines))