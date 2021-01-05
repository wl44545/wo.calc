from unittest import TestCase
from Calculator import Calculator


class Tests(TestCase):
	def setUp(self):
		self.calculator = Calculator(10, 'Word')


class TestImportValue(Tests):
	def test_dec_byte(self):
		self.calculator.set_system(10)
		self.calculator.set_word('Byte')

		self.calculator.clear()
		self.calculator.insert_whole_value('-128')
		self.assertEqual(self.calculator.display(), '-128')

		self.calculator.clear()
		self.calculator.insert_whole_value('127')
		self.assertEqual(self.calculator.display(), '127')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('-12')
		self.calculator.insert_step_value('9')
		self.assertEqual(self.calculator.display(), '-12')

		self.calculator.clear()
		self.calculator.insert_whole_value('12')
		self.calculator.insert_step_value('8')
		self.assertEqual(self.calculator.display(), '12')

	def test_oct_byte(self):
		self.calculator.set_system(8)
		self.calculator.set_word('Byte')

		self.calculator.clear()
		self.calculator.insert_whole_value('200')
		self.assertEqual(self.calculator.display(), '200')

		self.calculator.clear()
		self.calculator.insert_whole_value('177')
		self.assertEqual(self.calculator.display(), '177')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('40')
		self.calculator.insert_step_value('0')
		self.assertEqual(self.calculator.display(), '40')

		self.calculator.clear()
		self.calculator.insert_whole_value('50')
		self.calculator.insert_step_value('0')
		self.assertEqual(self.calculator.display(), '50')

	def test_hex_byte(self):
		self.calculator.set_system(16)
		self.calculator.set_word('Byte')

		self.calculator.clear()
		self.calculator.insert_whole_value('80')
		self.assertEqual(self.calculator.display(), '80')

		self.calculator.clear()
		self.calculator.insert_whole_value('7F')
		self.assertEqual(self.calculator.display(), '7F')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('FF')
		self.calculator.insert_step_value('7')
		self.assertEqual(self.calculator.display(), 'FF')

		self.calculator.clear()
		self.calculator.insert_whole_value('44')
		self.calculator.insert_step_value('4')
		self.assertEqual(self.calculator.display(), '44')

	def test_bin_byte(self):
		self.calculator.set_system(2)
		self.calculator.set_word('Byte')

		self.calculator.clear()
		self.calculator.insert_whole_value('11111111')
		self.assertEqual(self.calculator.display(), '11111111')

		self.calculator.clear()
		self.calculator.insert_whole_value('10000000')
		self.assertEqual(self.calculator.display(), '10000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('10000000')
		self.calculator.insert_step_value('0')
		self.assertEqual(self.calculator.display(), '10000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('10000001')
		self.calculator.insert_step_value('1')
		self.assertEqual(self.calculator.display(), '10000001')

	def test_dec_word(self):
		self.calculator.set_system(10)
		self.calculator.set_word('Word')

		self.calculator.clear()
		self.calculator.insert_whole_value('32767')
		self.assertEqual(self.calculator.display(), '32767')

		self.calculator.clear()
		self.calculator.insert_whole_value('-32768')
		self.assertEqual(self.calculator.display(), '-32768')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('3276')
		self.calculator.insert_step_value('8')
		self.assertEqual(self.calculator.display(), '3276')

		self.calculator.clear()
		self.calculator.insert_whole_value('-3276')
		self.calculator.insert_step_value('9')
		self.assertEqual(self.calculator.display(), '-3276')

	def test_oct_word(self):
		self.calculator.set_system(8)
		self.calculator.set_word('Word')

		self.calculator.clear()
		self.calculator.insert_whole_value('77777')
		self.assertEqual(self.calculator.display(), '77777')

		self.calculator.clear()
		self.calculator.insert_whole_value('100000')
		self.assertEqual(self.calculator.display(), '100000')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('77777')
		self.calculator.insert_step_value('7')
		self.assertEqual(self.calculator.display(), '77777')

		self.calculator.clear()
		self.calculator.insert_whole_value('44444')
		self.calculator.insert_step_value('4')
		self.assertEqual(self.calculator.display(), '44444')

	def test_hex_word(self):
		self.calculator.set_system(16)
		self.calculator.set_word('Word')

		self.calculator.clear()
		self.calculator.insert_whole_value('7FFF')
		self.assertEqual(self.calculator.display(), '7FFF')

		self.calculator.clear()
		self.calculator.insert_whole_value('8000')
		self.assertEqual(self.calculator.display(), '8000')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('7FFF')
		self.calculator.insert_step_value('F')
		self.assertEqual(self.calculator.display(), '7FFF')

		self.calculator.clear()
		self.calculator.insert_whole_value('8000')
		self.calculator.insert_step_value('0')
		self.assertEqual(self.calculator.display(), '8000')

	def test_bin_word(self):
		self.calculator.set_system(2)
		self.calculator.set_word('Word')

		self.calculator.clear()
		self.calculator.insert_whole_value('0111111111111111')
		self.assertEqual(self.calculator.display(), '0111111111111111')

		self.calculator.clear()
		self.calculator.insert_whole_value('1000000000000000')
		self.assertEqual(self.calculator.display(), '1000000000000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('1000000000000000')
		self.calculator.insert_step_value('0')
		self.assertEqual(self.calculator.display(), '1000000000000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('1111111111111111')
		self.calculator.insert_step_value('1')
		self.assertEqual(self.calculator.display(), '1111111111111111')
