from Letter import Letter
import fileinput
import sys

A = 65
default = []

def main() :
	op = sys.argv[1]
	filename = sys.argv[2]
	key = str(sys.argv[3]).upper()
	out_file = None
	
	if len(sys.argv) > 4 :
		out_file = sys.argv[4]
	
	# should create an array of alphabets using the key
	alphabets = get_alphabets(key)
	
	if op is "1" :
		print("Decrypting contents of " + filename)
		output = decrypt(filename, key, alphabets)
		
		if out_file is not None :
			outfile = open(out_file, "w")
			outfile.write(output)
			outfile.close()
		
		print(output)
	else :
		print("Encrypting contents of " + filename)
		output = encrypt(filename, key, alphabets)
		
		if out_file is not None :
			outfile = open(out_file, "w")
			outfile.write(output)
			outfile.close()
		
		print(output)

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
		
	for i in range(26) :
		value = 65 + i
		default.append(chr(value))
	
	return alphabets

def encrypt(filename, key, alphabets) :
	contents = get_contents(filename)
	lines = get_lines(contents)

	repeating = []
	for line in lines :
		index = 0
		repeat_line = ""
		for i in range(len(line)) :
			char = contents[i]
			
			if (Letter.isLetter(char)) :
				repeat_line = repeat_line + key[index % len(key)]
				index = index + 1
			else :
				repeat_line = repeat_line + char
		repeating.append(repeat_line)

	output = ""
	for line in lines :
		count = 0

		for i in range(len(line)) :
			target_char = line[i]

			if (Letter.isLetter(target_char)) :
				current_alphabet = alphabets[count]
				index = find_in_alphabet(target_char, default)
				out = current_alphabet[index]
				
				output = output + out
				count = count + 1
				if count > len(alphabets)-1 :
					count = 0
			else :
				output = output + target_char
		output = output + "\n"
	
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
	lines = get_lines(contents)
	
	output = ""
<<<<<<< HEAD
	current_alphabet = 0
	for char in contents:
		if (Letter.isLetter(char)):
			curr = Letter(char)
			mod = get_mod(alphabets[current_alphabet])
			
			cyphered = caesar_cypher(curr, mod)
			output = output + cyphered
			
			current_alphabet = current_alphabet + 1
			
			if current_alphabet > len(alphabets) :
				current_alphabet = 0
		else:
			output = output + char

# returns the difference between the current alphabet and the letter 'A'
def get_mod(curr) :
	start = ord(curr[0])
	a = ord('A')
	
	return start - a

=======
	for line in lines :
		count = 0
		for char in line :
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
		output = output + "\n"
	return output

def find_in_alphabet(letter, alphabet) :
	out = len(alphabet)
	for i in range(len(alphabet)) :
		if alphabet[i] is letter :
			out = i
	
	return out
			
>>>>>>> 56ce11d336e78d9308f33889e59fd50b356c651b
def get_contents(filename) :
	file = open(filename, "r")
	contents = file.read()
	contents = contents.upper()
	file.close()
	
	return contents

# given a string of multiple lines, return an array containing the lines with content
def get_lines(string) :
	output = string.split("\n")
	
	# remove lines that are just the empty string
	for i in range(len(output)) :
		for j in range(len(output)) :
			if output[j] is "" :
				output.pop(j)
				break

	return output

if len(sys.argv) >= 4 :
	main()
else :
<<<<<<< HEAD
	print("Enter an operation, file name, and a key")
=======
	print("To run this program, the additional command-line arguments are the operation: 1 to decrypt and anything else to encrypt; the source text file, the keyword, and an output file if one is desired.")
>>>>>>> 56ce11d336e78d9308f33889e59fd50b356c651b
