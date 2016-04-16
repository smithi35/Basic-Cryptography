import fileinput
from Letter import Letter

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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
def number_cypher(letter) :
	number = int(letter)
	number = number - 1
	actual = alphabet[number]
	
	return actual

def main() :
	file = open("Numbers.txt", "r")
	contents = file.read()
	contents = contents.upper()
	
	output = ""
	letter = ""
	for char in contents:
		# first get the letter
		
		if isNumber(char) :
			letter = letter + char
		else :
			if letter is not "" :
				output = output + number_cypher(letter)
			if not isDash(char) :
				output = output + char
			
			letter = ""

	print(output)

main()