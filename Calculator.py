import math as m


class Calculator:
	def __init__(self):
		self.system = 'DEC'
		self.word = 'Word'
		self.value = None

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

