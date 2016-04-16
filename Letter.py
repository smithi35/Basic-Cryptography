class Letter:
	bottom_number = 64
	top_number = 91
	
	def __init__(self, letter) :
		self.letter = letter[0]
		self.value = ord(letter) - Letter.bottom_number
		
	def get_letter(self) :
		return self.letter
	
	def get_value(self) :
		return self.value
	
	def isLetter(letter) :
		ascii = ord(letter)
		isL	= False
		
		if ((ascii > Letter.bottom_number) and (ascii < Letter.top_number)):
			isL = True;
		
		return isL