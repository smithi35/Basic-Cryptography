import fileinput
from Letter import Letter
	
# return the letter at the opposite end of the alphabet	
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

def main() :
	file = open("Caesar.txt", "r")
	mod = -3
	contents = file.read()
	contents = contents.upper()
	
	output = ""
	for char in contents:
		if (Letter.isLetter(char)):
			curr = Letter(char)
			cyphered = caesar_cypher(curr, mod)
			output = output + cyphered
		else:
			output = output + char
	
	print(output)
	file.close()
	file = open("output.txt", "w")
	file.write(output)

# test()
main()