from Letter import Letter
import fileinput
import sys

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

	# first create a string of the key repeating over and over
	length = len(contents)
	
	repeating = ""
	index = 0
	for i in range(len(contents)) :
		char = contents[i]
		
		if (Letter.isLetter(char)) :
			repeating = repeating + key[index % len(key)]
			index = index + 1
		else :
			repeating = repeating + char
	
	# now compare the two texts and create the encrypted text
	output = ""
	count = 0
	for i in range(len(contents)) :
		char = contents[i]
		
		if (Letter.isLetter(char)) :
			current_alphabet = alphabets[count]
			# using alphabets[count] find the letter at char's position
			char_value = ord(char)
			char_value = char_value - 65
			# print(char_value)
			output = output + current_alphabet[char_value]
			
			count = count + 1
			if count > len(alphabets)-1 :
				count = 0
		else :
			output = output + char
	
	return output

def decrypt(filename, key, alphabets) :
	contents = get_contents(filename)
	
	output = ""
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

def get_contents(filename) :
	file = open(filename, "r")
	contents = file.read()
	contents = contents.upper()
	
	return contents

if len(sys.argv) is 4 :
	main()
else :
	print("Enter an operation, file name, and a key")