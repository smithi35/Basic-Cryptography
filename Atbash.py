import fileinput
from Letter import Letter
	
# return the letter at the opposite end of the alphabet	
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

def main() :
	file = open("Atbash.txt", "r")
	contents = file.read()
	contents = contents.upper()
	
	output = ""
	for char in contents:
		if (Letter.isLetter(char)):
			curr = Letter(char)
			cyphered = atbash_cypher(curr)
			output = output + cyphered
		else:
			output = output + char
	
	print(output)
	file.close()
	file = open("output.txt", "w")
	file.write(output)
	file.close()

# test()
main()