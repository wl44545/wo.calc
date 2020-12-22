import math as m


class Calculator:
	def __init__(self):
		self.system = 'DEC'
		self.word = 'Word'
		self.current_value = None


######## lukasz

	def convert_system(self, value, input_system, output_system):
		pass

	def check_value_system(self, x): #czy liczba jest zgodna z systemem
		pass


########    monika
	def check_value_word(self, x): #czy wartość mieści się w słowie
		pass


######## w poniedzialek
	def insert_value(self, system, word, value):
		if system == 'DEC':
			converted_value = str(value)
		elif system == 'BIN':
			converted_value = int(str(value), 2)
		elif system == 'OCT':
			converted_value = int(str(value), 8)
		elif system == 'HEX':
			converted_value = int(str(value), 16)

		if word == "BYTE" and -128 <= int(converted_value) <= 127:
			self.value = converted_value
			return value



	def dodawanie(self, a, b):
		self.check_value_word(a)
		self.check_value_system(a)
		self.check_value_word(b)
		self.check_value_system(b)
		a1 = self.convert_system(a,self.system, 'Dec')
		b1 = self.convert_system(a,self.system, 'Dec')
		c = a + b
		self.check_value_word(c)
		self.check_value_system(c)
		return c