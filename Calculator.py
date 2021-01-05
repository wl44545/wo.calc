import math as m


class Calculator:
	def __init__(self, system, word):
		self.system = system
		self.word = word
		self.current_value = ''

	def set_system(self, system: int): #ustawia system liczbowy i konwertuje aktualna wartosc wyswietlacza
		if not self.current_value == '':
			self.current_value = self.convert_system(self.current_value, self.system, system)
		self.system = system

	def set_word(self, word: str): #ustawia dlugosc slowa
		self.word = word

	def clear(self): #czysci wyswietlacz
		self.current_value = ''

	def convert_system(self, value: str, input_system: int, output_system: int): #konwertuje liczbe z jednego systemu na drugi
		if input_system == output_system:
			return value
		dec = int(value, input_system)
		if output_system == 10:
			return dec
		elif output_system == 8:
			return oct(dec)[2:]
		elif output_system == 16:
			return hex(dec)[2:].upper()
		elif output_system == 2:
			return bin(dec)[2:]

	def check_value_system(self, value: str, system: int):  #sprawdza czy liczba jest zgodna z systemem
		allowed_chars = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
		value = value.upper()
		for char in value:
			if char not in allowed_chars[:system+1]:
				return False
		return True

	def check_value_word(self, value: str, word: str):  # sprawdza czy wartosc miesci sie w slowie
		return True

	def display(self):  # imituje wyswietlacz
		#print(self.current_value)
		return self.current_value

	def insert_whole_value(self, value: str):  # wprowadza cala liczbe, np. skopiowana
		if self.check_value_system(value, self.system) and self.check_value_word(value, self.word):
			self.current_value = value

	def insert_step_value(self, step: str):  # wprowadzanie liczby znak po znaku
		tmp = self.current_value + step
		if self.check_value_system(tmp, self.system) and self.check_value_word(tmp, self.word):
			self.current_value = tmp

	def add(self, a:str, b:str):
		c = str(int(a) + int(b))
		if self.check_value_system(c, self.system) and self.check_value_word(c, self.word):
			self.current_value = c
			return c

	def sub(self, a:str, b:str):
		c = str(int(a) - int(b))
		if self.check_value_system(c, self.system) and self.check_value_word(c, self.word):
			self.current_value = c
			return c

	def mul(self, a:str, b:str):
		c = str(int(a) * int(b))
		if self.check_value_system(c, self.system) and self.check_value_word(c, self.word):
			self.current_value = c
			return c

	def div(self, a:str, b:str):
		c = str(int(int(a) / int(b)))
		if self.check_value_system(c, self.system) and self.check_value_word(c, self.word):
			self.current_value = c
			return c

	def _neg(self, a:str):
		c = str(~int(a)+1)
		if self.check_value_system(c, self.system) and self.check_value_word(c, self.word):
			self.current_value = c
			return c

	def _and(self, a:str, b:str):
		c = str(int(a) & int(b))
		self.current_value = c
		return c

	def _or(self, a:str, b:str):
		c = str(int(a) | int(b))
		self.current_value = c
		return c

	def _xor(self, a:str, b:str):
		c = str(int(a) ^ int(b))
		self.current_value = c
		return c

	def _not(self, a:str):
		c = str(~int(a))
		if self.check_value_system(c, self.system) and self.check_value_word(c, self.word):
			self.current_value = c
			return c