from unittest import TestCase
from Calculator import Calculator


class Tests(TestCase):
	def setUp(self):
		self.calculator = Calculator(10, 'Word')


class TestInsertValue(Tests):
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

	def test_dec_dword(self):
		self.calculator.set_system(10)
		self.calculator.set_word('DWord')

		self.calculator.clear()
		self.calculator.insert_whole_value('2147483647')
		self.assertEqual(self.calculator.display(), '2147483647')

		self.calculator.clear()
		self.calculator.insert_whole_value('-2147483648')
		self.assertEqual(self.calculator.display(), '-2147483648')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('214748364')
		self.calculator.insert_step_value('8')
		self.assertEqual(self.calculator.display(), '214748364')

		self.calculator.clear()
		self.calculator.insert_whole_value('-214748364')
		self.calculator.insert_step_value('9')
		self.assertEqual(self.calculator.display(), '-214748364')

	def test_oct_dword(self):
		self.calculator.set_system(8)
		self.calculator.set_word('DWord')

		self.calculator.clear()
		self.calculator.insert_whole_value('17777777777')
		self.assertEqual(self.calculator.display(), '17777777777')

		self.calculator.clear()
		self.calculator.insert_whole_value('20000000000')
		self.assertEqual(self.calculator.display(), '20000000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('7777777777')
		self.calculator.insert_step_value('7')
		self.assertEqual(self.calculator.display(), '7777777777')

		self.calculator.clear()
		self.calculator.insert_whole_value('20000000000')
		self.calculator.insert_step_value('0')
		self.assertEqual(self.calculator.display(), '20000000000')

	def test_hex_dword(self):
		self.calculator.set_system(16)
		self.calculator.set_word('DWord')

		self.calculator.clear()
		self.calculator.insert_whole_value('7FFFFFFF')
		self.assertEqual(self.calculator.display(), '7FFFFFFF')

		self.calculator.clear()
		self.calculator.insert_whole_value('80000000')
		self.assertEqual(self.calculator.display(), '80000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('7FFFFFFF')
		self.calculator.insert_step_value('F')
		self.assertEqual(self.calculator.display(), '7FFFFFFF')

		self.calculator.clear()
		self.calculator.insert_whole_value('80000000')
		self.calculator.insert_step_value('0')
		self.assertEqual(self.calculator.display(), '80000000')

	def test_bin_dword(self):
		self.calculator.set_system(2)
		self.calculator.set_word('DWord')

		self.calculator.clear()
		self.calculator.insert_whole_value('01111111111111111111111111111111')
		self.assertEqual(self.calculator.display(), '01111111111111111111111111111111')

		self.calculator.clear()
		self.calculator.insert_whole_value('10000000000000000000000000000000')
		self.assertEqual(self.calculator.display(), '10000000000000000000000000000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('11111111111111111111111111111111')
		self.calculator.insert_step_value('1')
		self.assertEqual(self.calculator.display(), '11111111111111111111111111111111')

		self.calculator.clear()
		self.calculator.insert_whole_value('10000000000000000000000000000000')
		self.calculator.insert_step_value('0')
		self.assertEqual(self.calculator.display(), '10000000000000000000000000000000')

	def test_dec_qword(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator.clear()
		self.calculator.insert_whole_value('9223372036854775807')
		self.assertEqual(self.calculator.display(), '9223372036854775807')

		self.calculator.clear()
		self.calculator.insert_whole_value('-9223372036854775808')
		self.assertEqual(self.calculator.display(), '-9223372036854775808')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('922337203685477580')
		self.calculator.insert_step_value('8')
		self.assertEqual(self.calculator.display(), '922337203685477580')

		self.calculator.clear()
		self.calculator.insert_whole_value('-922337203685477580')
		self.calculator.insert_step_value('9')
		self.assertEqual(self.calculator.display(), '-922337203685477580')

	def test_oct_qword(self):
		self.calculator.set_system(8)
		self.calculator.set_word('QWord')

		self.calculator.clear()
		self.calculator.insert_whole_value('777777777777777777777')
		self.assertEqual(self.calculator.display(), '777777777777777777777')

		self.calculator.clear()
		self.calculator.insert_whole_value('1000000000000000000000')
		self.assertEqual(self.calculator.display(), '1000000000000000000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('777777777777777777777')
		self.calculator.insert_step_value('7')
		self.assertEqual(self.calculator.display(), '777777777777777777777')

		self.calculator.clear()
		self.calculator.insert_whole_value('1111111111111111111111')
		self.calculator.insert_step_value('1')
		self.assertEqual(self.calculator.display(), '1111111111111111111111')

	def test_hex_qword(self):
		self.calculator.set_system(16)
		self.calculator.set_word('QWord')

		self.calculator.clear()
		self.calculator.insert_whole_value('7FFFFFFFFFFFFFFF')
		self.assertEqual(self.calculator.display(), '7FFFFFFFFFFFFFFF')

		self.calculator.clear()
		self.calculator.insert_whole_value('8000000000000000')
		self.assertEqual(self.calculator.display(), '8000000000000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('0')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator.clear()
		self.calculator.insert_whole_value('FFFFFFFFFFFFFFFF')
		self.calculator.insert_step_value('F')
		self.assertEqual(self.calculator.display(), 'FFFFFFFFFFFFFFFF')

		self.calculator.clear()
		self.calculator.insert_whole_value('8000000000000000')
		self.calculator.insert_step_value('8')
		self.assertEqual(self.calculator.display(), '8000000000000000')

	def test_bin_qword(self):
		self.calculator.set_system(2)
		self.calculator.set_word('QWord')

		self.calculator.clear()
		self.calculator.insert_whole_value('0111111111111111111111111111111111111111111111111111111111111111')
		self.assertEqual(self.calculator.display(), '0111111111111111111111111111111111111111111111111111111111111111')

		self.calculator.clear()
		self.calculator.insert_whole_value('1000000000000000000000000000000000000000000000000000000000000000')
		self.assertEqual(self.calculator.display(), '1000000000000000000000000000000000000000000000000000000000000000')

		self.calculator.clear()
		self.calculator.insert_whole_value('1111111111111111111111111111111111111111111111111111111111111111')
		self.calculator.insert_step_value('1')
		self.assertEqual(self.calculator.display(), '1111111111111111111111111111111111111111111111111111111111111111')

		self.calculator.clear()
		self.calculator.insert_whole_value('1000000000000000000000000000000000000000000000000000000000000000')
		self.calculator.insert_step_value('1')
		self.assertEqual(self.calculator.display(), '1000000000000000000000000000000000000000000000000000000000000000')


class TestConvertValueSystem(Tests):
	def test_dec_oct(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(10)
		self.calculator.clear()
		self.calculator.insert_whole_value('100000')
		self.calculator.set_system(8)
		self.assertEqual(self.calculator.display(), '303240')

		self.calculator.set_system(10)
		self.calculator.clear()
		self.calculator.insert_whole_value('-100000')
		self.calculator.set_system(8)
		self.assertEqual(self.calculator.display(), '1777777777777777474540')

	def test_dec_hex(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(10)
		self.calculator.clear()
		self.calculator.insert_whole_value('100000')
		self.calculator.set_system(16)
		self.assertEqual(self.calculator.display(), '186A0')

		self.calculator.set_system(10)
		self.calculator.clear()
		self.calculator.insert_whole_value('-100000')
		self.calculator.set_system(16)
		self.assertEqual(self.calculator.display(), 'FFFFFFFFFFFE7960')

	def test_dec_bin(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(10)
		self.calculator.clear()
		self.calculator.insert_whole_value('100000')
		self.calculator.set_system(2)
		self.assertEqual(self.calculator.display(), '00011000011010100000')

		self.calculator.set_system(10)
		self.calculator.clear()
		self.calculator.insert_whole_value('-100000')
		self.calculator.set_system(2)
		self.assertEqual(self.calculator.display(), '1111111111111111111111111111111111111111111111100111100101100000')

	def test_oct_dec(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(8)
		self.calculator.clear()
		self.calculator.insert_whole_value('303240')
		self.calculator.set_system(10)
		self.assertEqual(self.calculator.display(), '100000')

		self.calculator.set_system(8)
		self.calculator.clear()
		self.calculator.insert_whole_value('1777777777777777474540')
		self.calculator.set_system(10)
		self.assertEqual(self.calculator.display(), '-100000')

	def test_oct_hex(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(8)
		self.calculator.clear()
		self.calculator.insert_whole_value('303240')
		self.calculator.set_system(16)
		self.assertEqual(self.calculator.display(), '186A0')

		self.calculator.set_system(8)
		self.calculator.clear()
		self.calculator.insert_whole_value('1777777777777777474540')
		self.calculator.set_system(16)
		self.assertEqual(self.calculator.display(), 'FFFFFFFFFFE7960')

	def test_oct_bin(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(8)
		self.calculator.clear()
		self.calculator.insert_whole_value('303240')
		self.calculator.set_system(2)
		self.assertEqual(self.calculator.display(), '00011000011010100000')

		self.calculator.set_system(8)
		self.calculator.clear()
		self.calculator.insert_whole_value('1777777777777777474540')
		self.calculator.set_system(2)
		self.assertEqual(self.calculator.display(), '1111111111111111111111111111111111111111111111100111100101100000')

	def test_hex_dec(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(16)
		self.calculator.clear()
		self.calculator.insert_whole_value('186A0')
		self.calculator.set_system(10)
		self.assertEqual(self.calculator.display(), '100000')

		self.calculator.set_system(16)
		self.calculator.clear()
		self.calculator.insert_whole_value('FFFFFFFFFFFE7960')
		self.calculator.set_system(10)
		self.assertEqual(self.calculator.display(), '-100000')

	def test_hex_oct(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(16)
		self.calculator.clear()
		self.calculator.insert_whole_value('186A0')
		self.calculator.set_system(8)
		self.assertEqual(self.calculator.display(), '303240')

		self.calculator.set_system(16)
		self.calculator.clear()
		self.calculator.insert_whole_value('FFFFFFFFFFFE7960')
		self.calculator.set_system(8)
		self.assertEqual(self.calculator.display(), '1777777777777777474540')

	def test_hex_bin(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(16)
		self.calculator.clear()
		self.calculator.insert_whole_value('186A0')
		self.calculator.set_system(2)
		self.assertEqual(self.calculator.display(), '00011000011010100000')

		self.calculator.set_system(16)
		self.calculator.clear()
		self.calculator.insert_whole_value('FFFFFFFFFFFE7960')
		self.calculator.set_system(2)
		self.assertEqual(self.calculator.display(), '1111111111111111111111111111111111111111111111100111100101100000')

	def test_bin_dec(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(2)
		self.calculator.clear()
		self.calculator.insert_whole_value('00011000011010100000')
		self.calculator.set_system(10)
		self.assertEqual(self.calculator.display(), '100000')

		self.calculator.set_system(2)
		self.calculator.clear()
		self.calculator.insert_whole_value('1111111111111111111111111111111111111111111111100111100101100000')
		self.calculator.set_system(10)
		self.assertEqual(self.calculator.display(), '-100000')

	def test_bin_oct(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(2)
		self.calculator.clear()
		self.calculator.insert_whole_value('00011000011010100000')
		self.calculator.set_system(8)
		self.assertEqual(self.calculator.display(), '303240')

		self.calculator.set_system(2)
		self.calculator.clear()
		self.calculator.insert_whole_value('1111111111111111111111111111111111111111111111100111100101100000')
		self.calculator.set_system(8)
		self.assertEqual(self.calculator.display(), '1777777777777777474540')

	def test_bin_hex(self):
		self.calculator.set_word('QWord')

		self.calculator.set_system(2)
		self.calculator.clear()
		self.calculator.insert_whole_value('00011000011010100000')
		self.calculator.set_system(16)
		self.assertEqual(self.calculator.display(), '186A0')

		self.calculator.set_system(2)
		self.calculator.clear()
		self.calculator.insert_whole_value('1111111111111111111111111111111111111111111111100111100101100000')
		self.calculator.set_system(16)
		self.assertEqual(self.calculator.display(), 'FFFFFFFFFFFE7960')


class TestConvertValueWord(Tests):
	def test_byte_word(self):
		self.calculator.set_system(10)

		self.calculator.set_word('Byte')
		self.calculator.clear()
		self.calculator.insert_whole_value('127')
		self.calculator.set_word('Word')
		self.assertEqual(self.calculator.display(), '127')

	def test_byte_dword(self):
		self.calculator.set_system(10)

		self.calculator.set_word('Byte')
		self.calculator.clear()
		self.calculator.insert_whole_value('127')
		self.calculator.set_word('DWord')
		self.assertEqual(self.calculator.display(), '127')

	def test_byte_qword(self):
		self.calculator.set_system(10)

		self.calculator.set_word('Byte')
		self.calculator.clear()
		self.calculator.insert_whole_value('127')
		self.calculator.set_word('QWord')
		self.assertEqual(self.calculator.display(), '127')

	def test_word_byte(self):
		self.calculator.set_system(10)

		self.calculator.set_word('Word')
		self.calculator.clear()
		self.calculator.insert_whole_value('127')
		self.calculator.set_word('Byte')
		self.assertEqual(self.calculator.display(), '127')

		self.calculator.set_word('Word')
		self.calculator.clear()
		self.calculator.insert_whole_value('256')
		self.calculator.set_word('Byte')
		self.assertEqual(self.calculator.display(), '0')

	def test_word_dword(self):
		self.calculator.set_system(10)

		self.calculator.set_word('Word')
		self.calculator.clear()
		self.calculator.insert_whole_value('127')
		self.calculator.set_word('DWord')
		self.assertEqual(self.calculator.display(), '127')

	def test_word_qword(self):
		self.calculator.set_system(10)

		self.calculator.set_word('Word')
		self.calculator.clear()
		self.calculator.insert_whole_value('127')
		self.calculator.set_word('QWord')
		self.assertEqual(self.calculator.display(), '127')

	def test_dword_byte(self):
		self.calculator.set_system(10)

		self.calculator.set_word('DWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('127')
		self.calculator.set_word('Byte')
		self.assertEqual(self.calculator.display(), '127')

		self.calculator.set_word('DWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('65536')
		self.calculator.set_word('Byte')
		self.assertEqual(self.calculator.display(), '0')

	def test_dword_word(self):
		self.calculator.set_system(10)

		self.calculator.set_word('DWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('16384')
		self.calculator.set_word('Word')
		self.assertEqual(self.calculator.display(), '16384')

		self.calculator.set_word('DWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('65536')
		self.calculator.set_word('Word')
		self.assertEqual(self.calculator.display(), '0')

	def test_dword_qword(self):
		self.calculator.set_system(10)

		self.calculator.set_word('DWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('4194304')
		self.calculator.set_word('QWord')
		self.assertEqual(self.calculator.display(), '4194304')

	def test_qword_byte(self):
		self.calculator.set_system(10)

		self.calculator.set_word('QWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('127')
		self.calculator.set_word('Byte')
		self.assertEqual(self.calculator.display(), '127')

		self.calculator.set_word('QWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('256')
		self.calculator.set_word('Byte')
		self.assertEqual(self.calculator.display(), '0')

	def test_qword_word(self):
		self.calculator.set_system(10)

		self.calculator.set_word('QWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('16384')
		self.calculator.set_word('Word')
		self.assertEqual(self.calculator.display(), '16384')

		self.calculator.set_word('QWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('32768')
		self.calculator.set_word('Word')
		self.assertEqual(self.calculator.display(), '-32768')

	def test_qword_dword(self):
		self.calculator.set_system(10)

		self.calculator.set_word('QWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('32768')
		self.calculator.set_word('DWord')
		self.assertEqual(self.calculator.display(), '32768')

		self.calculator.set_word('QWord')
		self.calculator.clear()
		self.calculator.insert_whole_value('141312929864')
		self.calculator.set_word('DWord')
		self.assertEqual(self.calculator.display(), '-420990904')


class TestArithmetics(Tests):
	def test_add(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator.add('10', '5')
		self.assertEqual(self.calculator.display(), '15')

		self.calculator.add('3', '4')
		self.assertEqual(self.calculator.display(), '7')

		self.calculator.add('10', '5')
		self.assertNotEqual(self.calculator.display(), '13')

		self.calculator.add('3', '4')
		self.assertNotEqual(self.calculator.display(), '2')

	def test_sub(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator.sub('10', '5')
		self.assertEqual(self.calculator.display(), '5')

		self.calculator.sub('3', '4')
		self.assertEqual(self.calculator.display(), '-1')

		self.calculator.sub('10', '5')
		self.assertNotEqual(self.calculator.display(), '13')

		self.calculator.sub('3', '4')
		self.assertNotEqual(self.calculator.display(), '2')

	def test_mul(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator.mul('10', '5')
		self.assertEqual(self.calculator.display(), '50')

		self.calculator.mul('3', '4')
		self.assertEqual(self.calculator.display(), '12')

		self.calculator.mul('10', '5')
		self.assertNotEqual(self.calculator.display(), '13')

		self.calculator.mul('3', '4')
		self.assertNotEqual(self.calculator.display(), '2')

	def test_div(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator.div('10', '5')
		self.assertEqual(self.calculator.display(), '2')

		self.calculator.div('4', '4')
		self.assertEqual(self.calculator.display(), '1')

		self.calculator.div('10', '5')
		self.assertNotEqual(self.calculator.display(), '13')

		self.calculator.div('3', '4')
		self.assertNotEqual(self.calculator.display(), '2')

	def test_neg(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator._neg('10')
		self.assertEqual(self.calculator.display(), '-10')

		self.calculator._neg('4')
		self.assertEqual(self.calculator.display(), '-4')

		self.calculator._neg('10')
		self.assertNotEqual(self.calculator.display(), '13')

		self.calculator._neg('4')
		self.assertNotEqual(self.calculator.display(), '2')

	def test_and(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator._and('10', '5')
		self.assertEqual(self.calculator.display(), '0')

		self.calculator._and('12', '8')
		self.assertEqual(self.calculator.display(), '8')

		self.calculator._and('10', '5')
		self.assertNotEqual(self.calculator.display(), '2')

		self.calculator._and('12', '8')
		self.assertNotEqual(self.calculator.display(), '3')

	def test_or(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator._or('10', '5')
		self.assertEqual(self.calculator.display(), '15')

		self.calculator._or('12', '8')
		self.assertEqual(self.calculator.display(), '12')

		self.calculator._or('10', '5')
		self.assertNotEqual(self.calculator.display(), '4')

		self.calculator._or('12', '8')
		self.assertNotEqual(self.calculator.display(), '32')

	def test_xor(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator._xor('10', '5')
		self.assertEqual(self.calculator.display(), '15')

		self.calculator._xor('12', '8')
		self.assertEqual(self.calculator.display(), '4')

		self.calculator._xor('10', '5')
		self.assertNotEqual(self.calculator.display(), '3')

		self.calculator._xor('12', '8')
		self.assertNotEqual(self.calculator.display(), '12')

	def test_not(self):
		self.calculator.set_system(10)
		self.calculator.set_word('QWord')

		self.calculator._not('10')
		self.assertEqual(self.calculator.display(), '-11')

		self.calculator._not('12')
		self.assertEqual(self.calculator.display(), '-13')

		self.calculator._not('10')
		self.assertNotEqual(self.calculator.display(), '15')

		self.calculator._not('4')
		self.assertNotEqual(self.calculator.display(), '-133')




