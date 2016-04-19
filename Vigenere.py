from Letter import Letter
import fileinput
import sys

A = 65

def main() :
	op = sys.argv[1]
	filename = sys.argv[2]
	key = str(sys.argv[3]).upper()
	
	# should create an array of alphabets using the key
	alphabets = get_alphabets(key)
	
	if op is "1" :
		print("Decrypting contents of " + filename)
		output = decrypt(filename, key, alphabets)
		print(output)
	else :
		print("Encrypting contents of " + filename)
		# output = open("output.txt", "w")
		output_string = encrypt(filename, key, alphabets)
		print(output_string)

def get_alphabets(key) :
	alphabets = []
	
	for letter in key :
		current = []
		letter = ord(letter)
		
		for i in range(26) :
			current.append("" + chr(letter))
			letter = letter + 1
			if letter > 90 :
				letter = 65
		
		alphabets.append(current)
	return alphabets

def encrypt(filename, key, alphabets) :
	contents = get_contents(filename)

	repeating = ""
	index = 0
	for i in range(len(contents)) :
		char = contents[i]
		
		if (Letter.isLetter(char)) :
			repeating = repeating + key[index % len(key)]
			index = index + 1
		else :
			repeating = repeating + char

	output = ""
	count = 0
	for i in range(len(contents)) :
		target_char = contents[i]
		
		if (Letter.isLetter(target_char)) :
			target_value = Letter(target_char).get_value() -1
			repeat_char = repeating[i]
			repeat_value = Letter(repeat_char).get_value() -1
			shift = ((target_value + repeat_value) % 26) + 65
			out = chr(shift)
			
			output = output + out
			count = count + 1
			if count > len(alphabets)-1 :
				count = 0
		else :
			output = output + target_char
	
	return output
	
def caesar_cypher(letter, mod) :
	value = letter.get_value()
	value = value + mod
	
	if (value < 1) :
		value = value + 26
	elif (value > 26) :
		value = value % 26
		value = value + 1
	
	value = value + Letter.bottom_number
	return chr(value-1)


def decrypt(filename, key, alphabets) :
	contents = get_contents(filename)
	
	# split contents by newline characters?
	lines = contents.split("\n")
	print(lines)
	exit()
	
	output = ""
	count = 0
	for char in contents:
		if (Letter.isLetter(char)):
			current_alphabet = alphabets[count]
			
			repeat_value = find_in_alphabet(char, current_alphabet)
			
			char_value = 65 + repeat_value
			output = output + chr(char_value)
			
			count = count + 1
			if count > len(alphabets) -1:
				count = 0
		else:
			output = output + char

	return output

def find_in_alphabet(letter, alphabet) :
	out = len(alphabet)
	for i in range(len(alphabet)) :
		if alphabet[i] is letter :
			out = i
	
	return out

def get_mod(alphabet) :
	mod = 0 + ord(alphabet[0]) - 65
	return mod
			
def get_contents(filename) :
	file = open(filename, "r")
	contents = file.read()
	contents = contents.upper()
	
	return contents

# given a string of multiple lines, return an array containing the lines with content
def get_lines(string) :
	output = string.split("\n")
	
	# remove lines that are just the empty string
	

if len(sys.argv) is 4 :
	main()
else :
	print("Enter a file name and a key")