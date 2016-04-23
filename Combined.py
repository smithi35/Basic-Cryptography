import fileinput
from Letter import Letter
	
# return the letter at the opposite end of the alphabet	
def main() :
	file = open("Combined.txt", "r")
	contents = file.read()
	contents = contents.upper()
	
	# start with A1Z26, then Atbash, then Caesar
	contents = a1z26(contents)
	contents = atbash(contents)
	mod = -3
	contents = caesar(contents, mod)
	
	file.close()
	file = open("output.txt", "w")
	file.write(contents)
	file.close()
	print("Decrypted contents sent to output.txt")

def a1z26(contents) :
	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	output = ""
	letter = ""
	for char in contents:
		# first get the letter
		
		if isNumber(char) :
			letter = letter + char
		else :
			if letter is not "" :
				output = output + a1z26_cypher(letter, alphabet)
			if not isDash(char) :
				output = output + char
			
			letter = ""
			
	if letter is not "" :
		output = output + a1z26_cypher(letter, alphabet)

	return output

def isDash(char) :
	ascii = ord(char)
	isD = False
	
	if ascii is 45:
		isD = True;
	
	return isD

def isNumber(char) :
	ascii = ord(char)
	isN = False
	
	if ascii > 47 and ascii < 58 :
		isN = True
		
	return isN

# return the letter at the opposite end of the alphabet	
def a1z26_cypher(letter, alphabet) :
	number = int(letter)
	number = number - 1
	actual = alphabet[number]
	
	return actual
	
def atbash(contents) :
	output = ""
	for char in contents:
		if (Letter.isLetter(char)):
			curr = Letter(char)
			cyphered = atbash_cypher(curr)
			output = output + cyphered
		else:
			output = output + char
	
	return output
	
def atbash_cypher(letter) :
	value = letter.get_value()
	index = 0
	
	if (value <= 13) :
		index = 26
		for i in range(1, value):
			index = index - 1
		
	else :# value >= 14
		index = 1
		for i in range(value, 26):
			index = index + 1
	
	# convert index to a letter
	index = index + Letter.bottom_number
	return chr(index)

def caesar(contents, mod) :
	output = ""
	for char in contents:
		if (Letter.isLetter(char)):
			curr = Letter(char)
			cyphered = caesar_cypher(curr, mod)
			output = output + cyphered
		else:
			output = output + char
	
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
	return chr(value)

	
# test()
main()