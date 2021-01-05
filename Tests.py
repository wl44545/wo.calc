from unittest import TestCase
from Calculator import Calculator


class Tests(TestCase):
	def setUp(self):
		self.calculator = Calculator(10, 'Word')


class TestImportValue(Tests):
	def test_dec_byte_positive(self):
		self.assertEqual(self.calculator.insert_value('DEC', 'BYTE', 127), 127)
		self.assertEqual(self.calculator.insert_value('DEC', 'BYTE', 0), 0)
		self.assertEqual(self.calculator.insert_value('DEC', 'BYTE', -128), -128)

		self.assertEqual(self.calculator.insert_value('OCT', 'BYTE', '0o200'), '0o200')
		self.assertEqual(self.calculator.insert_value('OCT', 'BYTE', '0o400'), '0o400')


	def test_dec_byte_negative(self):
		self.assertNotEqual(self.calculator.insert_value('DEC', 'BYTE', 128), 128)
		self.assertNotEqual(self.calculator.insert_value('DEC', 'BYTE', -129), -129)
