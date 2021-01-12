package Calculator;
import org.junit.Assert;
import org.junit.jupiter.api.Test;

class Tests {

	@Test
	void test_dec_byte(){
		Calculator calculator = new Calculator(10, "Byte");
		calculator.clear();
		calculator.insert_whole_value("-128");
		Assert.assertEquals(calculator.display(), "-128");

		calculator.clear();
		calculator.insert_whole_value("127");
		Assert.assertEquals(calculator.display(), "127");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("-12");
		calculator.insert_step_value("9");
		Assert.assertEquals(calculator.display(), "-12");

		calculator.clear();
		calculator.insert_whole_value("12");
		calculator.insert_step_value("8");
		Assert.assertEquals(calculator.display(), "12");
	}
	@Test
	void test_oct_byte(){
		Calculator calculator = new Calculator(8, "Byte");
		
		calculator.clear();
		calculator.insert_whole_value("200");
		Assert.assertEquals(calculator.display(), "200");

		calculator.clear();
		calculator.insert_whole_value("177");
		Assert.assertEquals(calculator.display(), "177");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("40");
		calculator.insert_step_value("0");
		Assert.assertEquals(calculator.display(), "40");

		calculator.clear();
		calculator.insert_whole_value("50");
		calculator.insert_step_value("0");
		Assert.assertEquals(calculator.display(), "50");
	}
	@Test
	void test_hex_byte(){
		Calculator calculator = new Calculator(16, "Byte");

		calculator.clear();
		calculator.insert_whole_value("70");
		Assert.assertEquals(calculator.display(), "70");

		calculator.clear();
		calculator.insert_whole_value("7E");
		Assert.assertEquals(calculator.display(), "7E");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("11");
		calculator.insert_step_value("7");
		Assert.assertEquals(calculator.display(), "11");

		calculator.clear();
		calculator.insert_whole_value("44");
		calculator.insert_step_value("4");
		
		Assert.assertEquals(calculator.display(), "44");
	}
	@Test
	void test_bin_byte(){
		Calculator calculator = new Calculator(2, "Byte");

		calculator.clear();
		calculator.insert_whole_value("11111111");
		Assert.assertEquals(calculator.display(), "11111111");

		calculator.clear();
		calculator.insert_whole_value("10000000");
		Assert.assertEquals(calculator.display(), "10000000");

		calculator.clear();
		calculator.insert_whole_value("10000000");
		calculator.insert_step_value("0");
		Assert.assertEquals(calculator.display(), "10000000");

		calculator.clear();
		calculator.insert_whole_value("10000001");
		calculator.insert_step_value("1");
		Assert.assertEquals(calculator.display(), "10000001");
	}
	@Test
	void test_dec_word(){
		Calculator calculator = new Calculator(10, "Word");

		calculator.clear();
		calculator.insert_whole_value("32767");
		Assert.assertEquals(calculator.display(), "32767");

		calculator.clear();
		calculator.insert_whole_value("-32768");
		Assert.assertEquals(calculator.display(), "-32768");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("3276");
		calculator.insert_step_value("8");
		Assert.assertEquals(calculator.display(), "3276");

		calculator.clear();
		calculator.insert_whole_value("-3276");
		calculator.insert_step_value("9");
		Assert.assertEquals(calculator.display(), "-3276");
	}
	@Test
	void test_oct_word(){
		Calculator calculator = new Calculator(8, "Word");

		calculator.clear();
		calculator.insert_whole_value("77777");
		Assert.assertEquals(calculator.display(), "77777");

		calculator.clear();
		calculator.insert_whole_value("100000");
		Assert.assertEquals(calculator.display(), "100000");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("77777");
		calculator.insert_step_value("7");
		Assert.assertEquals(calculator.display(), "77777");

		calculator.clear();
		calculator.insert_whole_value("44444");
		calculator.insert_step_value("4");
		Assert.assertEquals(calculator.display(), "44444");
	}
	@Test
	void test_hex_word(){
		Calculator calculator = new Calculator(16, "Word");

		calculator.clear();
		calculator.insert_whole_value("7FFF");
		Assert.assertEquals(calculator.display(), "7FFF");

		calculator.clear();
		calculator.insert_whole_value("7000");
		Assert.assertEquals(calculator.display(), "7000");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("7FFF");
		calculator.insert_step_value("F");
		Assert.assertEquals(calculator.display(), "7FFF");

		calculator.clear();
		calculator.insert_whole_value("7000");
		calculator.insert_step_value("0");
		Assert.assertEquals(calculator.display(), "7000");
	}
	@Test
	void test_bin_word(){
		Calculator calculator = new Calculator(2, "Word");

		calculator.clear();
		calculator.insert_whole_value("0111111111111111");
		Assert.assertEquals(calculator.display(), "0111111111111111");

		calculator.clear();
		calculator.insert_whole_value("1000000000000000");
		Assert.assertEquals(calculator.display(), "1000000000000000");

		calculator.clear();
		calculator.insert_whole_value("1000000000000000");
		calculator.insert_step_value("0");
		Assert.assertEquals(calculator.display(), "1000000000000000");

		calculator.clear();
		calculator.insert_whole_value("1111111111111111");
		calculator.insert_step_value("1");
		Assert.assertEquals(calculator.display(), "1111111111111111");
	}
	@Test
	void test_dec_dword(){
		Calculator calculator = new Calculator(10, "DWord");

		calculator.clear();
		calculator.insert_whole_value("2147483647");
		Assert.assertEquals(calculator.display(), "2147483647");

		calculator.clear();
		calculator.insert_whole_value("-2147483648");
		Assert.assertEquals(calculator.display(), "-2147483648");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("214748364");
		calculator.insert_step_value("8");
		Assert.assertEquals(calculator.display(), "214748364");

		calculator.clear();
		calculator.insert_whole_value("-214748364");
		calculator.insert_step_value("9");
		Assert.assertEquals(calculator.display(), "-214748364");
	}
	@Test
	void test_oct_dword(){
		Calculator calculator = new Calculator(8, "DWord");

		calculator.clear();
		calculator.insert_whole_value("17777777777");
		Assert.assertEquals(calculator.display(), "17777777777");

		calculator.clear();
		calculator.insert_whole_value("20000000000");
		Assert.assertEquals(calculator.display(), "20000000000");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("7777777777");
		calculator.insert_step_value("7");
		Assert.assertEquals(calculator.display(), "7777777777");

		calculator.clear();
		calculator.insert_whole_value("20000000000");
		calculator.insert_step_value("0");
		Assert.assertEquals(calculator.display(), "20000000000");
	}
	@Test
	void test_hex_dword(){
		Calculator calculator = new Calculator(16, "DWord");

		calculator.clear();
		calculator.insert_whole_value("7FFFFFFF");
		Assert.assertEquals(calculator.display(), "7FFFFFFF");

		calculator.clear();
		calculator.insert_whole_value("70000000");
		Assert.assertEquals(calculator.display(), "70000000");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("7FFFFFFF");
		calculator.insert_step_value("F");
		Assert.assertEquals(calculator.display(), "7FFFFFFF");

		calculator.clear();
		calculator.insert_whole_value("70000000");
		calculator.insert_step_value("0");
		Assert.assertEquals(calculator.display(), "70000000");
	}
	@Test
	void test_bin_dword(){
		Calculator calculator = new Calculator(2, "DWord");

		calculator.clear();
		calculator.insert_whole_value("01111111111111111111111111111111");
		Assert.assertEquals(calculator.display(), "01111111111111111111111111111111");

		calculator.clear();
		calculator.insert_whole_value("10000000000000000000000000000000");
		Assert.assertEquals(calculator.display(), "10000000000000000000000000000000");

		calculator.clear();
		calculator.insert_whole_value("11111111111111111111111111111111");
		calculator.insert_step_value("1");
		Assert.assertEquals(calculator.display(), "11111111111111111111111111111111");

		calculator.clear();
		calculator.insert_whole_value("10000000000000000000000000000000");
		calculator.insert_step_value("0");
		Assert.assertEquals(calculator.display(), "10000000000000000000000000000000");
	}
	@Test
	void test_dec_qword(){
		Calculator calculator = new Calculator(10, "QWord");

		calculator.clear();
		calculator.insert_whole_value("9223372036854775807");
		Assert.assertEquals(calculator.display(), "9223372036854775807");

		calculator.clear();
		calculator.insert_whole_value("-9223372036854775808");
		Assert.assertEquals(calculator.display(), "-9223372036854775808");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("922337203685477580");
		calculator.insert_step_value("8");
		Assert.assertEquals(calculator.display(), "922337203685477580");

		calculator.clear();
		calculator.insert_whole_value("-922337203685477580");
		calculator.insert_step_value("9");
		Assert.assertEquals(calculator.display(), "-922337203685477580");
	}
	@Test
	void test_oct_qword(){
		Calculator calculator = new Calculator(8, "QWord");

		calculator.clear();
		calculator.insert_whole_value("777777777777777777777");
		Assert.assertEquals(calculator.display(), "777777777777777777777");

		calculator.clear();
		calculator.insert_whole_value("1000000000000000000000");
		Assert.assertEquals(calculator.display(), "1000000000000000000000");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("777777777777777777777");
		calculator.insert_step_value("7");
		Assert.assertEquals(calculator.display(), "777777777777777777777");

		calculator.clear();
		calculator.insert_whole_value("1111111111111111111111");
		calculator.insert_step_value("1");
		Assert.assertEquals(calculator.display(), "1111111111111111111111");
	}
	@Test
	void test_hex_qword(){
		Calculator calculator = new Calculator(16, "QWord");

		calculator.clear();
		calculator.insert_whole_value("7FFFFFFFFFFFFFFF");
		Assert.assertEquals(calculator.display(), "7FFFFFFFFFFFFFFF");

		calculator.clear();
		calculator.insert_whole_value("7000000000000000");
		Assert.assertEquals(calculator.display(), "7000000000000000");

		calculator.clear();
		calculator.insert_whole_value("0");
		Assert.assertEquals(calculator.display(), "0");

		calculator.clear();
		calculator.insert_whole_value("7FFFFFFFFFFFFFFF");
		calculator.insert_step_value("F");
		Assert.assertEquals(calculator.display(), "7FFFFFFFFFFFFFF");

		calculator.clear();
		calculator.insert_whole_value("700000000000000");
		calculator.insert_step_value("8");
		Assert.assertEquals(calculator.display(), "700000000000000");
	}
	@Test
	void test_bin_qword(){
		Calculator calculator = new Calculator(2, "QWord");

		calculator.clear();
		calculator.insert_whole_value("0111111111111111111111111111111111111111111111111111111111111111");
		Assert.assertEquals(calculator.display(), "0111111111111111111111111111111111111111111111111111111111111111");

		calculator.clear();
		calculator.insert_whole_value("1000000000000000000000000000000000000000000000000000000000000000");
		Assert.assertEquals(calculator.display(), "1000000000000000000000000000000000000000000000000000000000000000");

		calculator.clear();
		calculator.insert_whole_value("1111111111111111111111111111111111111111111111111111111111111111");
		calculator.insert_step_value("1");
		Assert.assertEquals(calculator.display(), "1111111111111111111111111111111111111111111111111111111111111111");

		calculator.clear();
		calculator.insert_whole_value("1000000000000000000000000000000000000000000000000000000000000000");
		calculator.insert_step_value("1");
		Assert.assertEquals(calculator.display(), "1000000000000000000000000000000000000000000000000000000000000000");

	}
	@Test
	void test_dec_oct(){
		Calculator calculator = new Calculator(10, "QWord");

		calculator.clear();
		calculator.insert_whole_value("100000");
		calculator.set_system(8);
		Assert.assertEquals(calculator.display(), "303240");

		calculator.set_system(10);
		calculator.clear();
		calculator.insert_whole_value("-100000");
		calculator.set_system(8);
		Assert.assertEquals(calculator.display(), "37777474540");
	}
	@Test
	void test_dec_hex(){
		Calculator calculator = new Calculator(10, "QWord");

		calculator.clear();
		calculator.insert_whole_value("100000");
		calculator.set_system(16);
		Assert.assertEquals(calculator.display(), "186A0");

		calculator.set_system(10);
		calculator.clear();
		calculator.insert_whole_value("-100000");
		calculator.set_system(16);
		Assert.assertEquals(calculator.display(), "FFFE7960");
	}
	@Test
	void test_dec_bin(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("100000");
		calculator.set_system(2);
		Assert.assertEquals(calculator.display(), "11000011010100000");

		calculator.set_system(10);
		calculator.clear();
		calculator.insert_whole_value("-100000");
		calculator.set_system(2);
		Assert.assertEquals(calculator.display(), "11111111111111100111100101100000");
	}
	@Test
	void test_oct_dec(){
		Calculator calculator = new Calculator(8, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("303240");
		calculator.set_system(10);
		Assert.assertEquals(calculator.display(), "100000");

		calculator.set_system(8);
		calculator.clear();
		calculator.insert_whole_value("1777777777777777474540");
		calculator.set_system(10);
		Assert.assertEquals(calculator.display(), "-100000");
	}
	@Test
	void test_oct_hex(){
		Calculator calculator = new Calculator(8, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("303240");
		calculator.set_system(16);
		Assert.assertEquals(calculator.display(), "186A0");

		calculator.set_system(8);
		calculator.clear();
		calculator.insert_whole_value("1777777777777777474540");
		calculator.set_system(16);
		Assert.assertEquals(calculator.display(), "FFFFFFFFFFE7960");
	}
	@Test
	void test_oct_bin(){
		Calculator calculator = new Calculator(8, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("303240");
		calculator.set_system(2);
		Assert.assertEquals(calculator.display(), "00011000011010100000");

		calculator.set_system(8);
		calculator.clear();
		calculator.insert_whole_value("1777777777777777474540");
		calculator.set_system(2);
		Assert.assertEquals(calculator.display(), "1111111111111111111111111111111111111111111111100111100101100000");
	}
	@Test
	void test_hex_dec(){
		Calculator calculator = new Calculator(16, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("186A0");
		calculator.set_system(10);
		Assert.assertEquals(calculator.display(), "100000");

		calculator.set_system(16);
		calculator.clear();
		calculator.insert_whole_value("FFFFFFFFFFFE7960");
		calculator.set_system(10);
		Assert.assertEquals(calculator.display(), "-100000");
	}
	@Test
	void test_hex_oct(){
		Calculator calculator = new Calculator(16, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("186A0");
		calculator.set_system(8);
		Assert.assertEquals(calculator.display(), "303240");

		calculator.set_system(16);
		calculator.clear();
		calculator.insert_whole_value("FFFFFFFFFFFE7960");
		calculator.set_system(8);
		Assert.assertEquals(calculator.display(), "1777777777777777474540");
	}
	@Test
	void test_hex_bin(){
		Calculator calculator = new Calculator(16, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("186A0");
		calculator.set_system(2);
		Assert.assertEquals(calculator.display(), "00011000011010100000");

		calculator.set_system(16);
		calculator.clear();
		calculator.insert_whole_value("FFFFFFFFFFFE7960");
		calculator.set_system(2);
		Assert.assertEquals(calculator.display(), "1111111111111111111111111111111111111111111111100111100101100000");
	}
	@Test
	void test_bin_dec(){
		Calculator calculator = new Calculator(2, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("00011000011010100000");
		calculator.set_system(10);
		Assert.assertEquals(calculator.display(), "100000");

		calculator.set_system(2);
		calculator.clear();
		calculator.insert_whole_value("11100111100101100000");
		calculator.set_system(10);
		Assert.assertEquals(calculator.display(), "948576");
	}
	@Test
	void test_bin_oct(){
		Calculator calculator = new Calculator(2, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("00011000011010100000");
		calculator.set_system(8);
		Assert.assertEquals(calculator.display(), "303240");

		calculator.set_system(2);
		calculator.clear();
		calculator.insert_whole_value("11100111100101100000");
		calculator.set_system(8);
		Assert.assertEquals(calculator.display(), "3474540");
	}
	@Test
	void test_bin_hex(){
		Calculator calculator = new Calculator(2, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("00011000011010100000");
		calculator.set_system(16);
		Assert.assertEquals(calculator.display(), "186A0");

		calculator.set_system(2);
		calculator.clear();
		calculator.insert_whole_value("111100111100101100000");
		calculator.set_system(16);
		Assert.assertEquals(calculator.display(), "1E7960");


	}
	@Test
	void test_byte_word(){
		Calculator calculator = new Calculator(10, "Byte");
		
		calculator.clear();
		calculator.insert_whole_value("127");
		calculator.set_word("Word");
		Assert.assertEquals(calculator.display(), "127");
	}
	@Test
	void test_byte_dword(){
		Calculator calculator = new Calculator(10, "Byte");
		
		calculator.clear();
		calculator.insert_whole_value("127");
		calculator.set_word("DWord");
		Assert.assertEquals(calculator.display(), "127");
	}
	@Test
	void test_byte_qword(){
		Calculator calculator = new Calculator(10, "Byte");
		
		calculator.clear();
		calculator.insert_whole_value("127");
		calculator.set_word("QWord");
		Assert.assertEquals(calculator.display(), "127");
	}
	@Test
	void test_word_byte(){
		Calculator calculator = new Calculator(10, "Word");
		
		calculator.clear();
		calculator.insert_whole_value("127");
		calculator.set_word("Byte");
		Assert.assertEquals(calculator.display(), "127");

		calculator.set_word("Word");
		calculator.clear();
		calculator.insert_whole_value("256");
		calculator.set_word("Byte");
		Assert.assertEquals(calculator.display(), "0");
	}
	@Test
	void test_word_dword(){
		Calculator calculator = new Calculator(10, "Word");
		
		calculator.clear();
		calculator.insert_whole_value("127");
		calculator.set_word("DWord");
		Assert.assertEquals(calculator.display(), "127");
	}
	@Test
	void test_word_qword(){
		Calculator calculator = new Calculator(10, "Word");
		
		calculator.clear();
		calculator.insert_whole_value("127");
		calculator.set_word("QWord");
		Assert.assertEquals(calculator.display(), "127");
	}
	@Test
	void test_dword_byte(){
		Calculator calculator = new Calculator(10, "DWord");
		
		calculator.clear();
		calculator.insert_whole_value("127");
		calculator.set_word("Byte");
		Assert.assertEquals(calculator.display(), "127");

		calculator.set_word("DWord");
		calculator.clear();
		calculator.insert_whole_value("65536");
		calculator.set_word("Byte");
		Assert.assertEquals(calculator.display(), "0");
	}
	@Test
	void test_dword_word(){
		Calculator calculator = new Calculator(10, "DWord");
		
		calculator.clear();
		calculator.insert_whole_value("16384");
		calculator.set_word("Word");
		Assert.assertEquals(calculator.display(), "16384");

		calculator.set_word("DWord");
		calculator.clear();
		calculator.insert_whole_value("65536");
		calculator.set_word("Word");
		Assert.assertEquals(calculator.display(), "0");
	}
	@Test
	void test_dword_qword(){
		Calculator calculator = new Calculator(10, "DWord");
		
		calculator.clear();
		calculator.insert_whole_value("4194304");
		calculator.set_word("QWord");
		Assert.assertEquals(calculator.display(), "4194304");
	}
	@Test
	void test_qword_byte(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("127");
		calculator.set_word("Byte");
		Assert.assertEquals(calculator.display(), "127");

		calculator.set_word("QWord");
		calculator.clear();
		calculator.insert_whole_value("256");
		calculator.set_word("Byte");
		Assert.assertEquals(calculator.display(), "0");
	}
	@Test
	void test_qword_word(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("16384");
		calculator.set_word("Word");
		Assert.assertEquals(calculator.display(), "16384");

		calculator.set_word("QWord");
		calculator.clear();
		calculator.insert_whole_value("32768");
		calculator.set_word("Word");
		Assert.assertEquals(calculator.display(), "-32768");
	}
	@Test
	void test_qword_dword(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator.clear();
		calculator.insert_whole_value("32768");
		calculator.set_word("DWord");
		Assert.assertEquals(calculator.display(), "32768");

		calculator.set_word("QWord");
		calculator.clear();
		calculator.insert_whole_value("141312929864");
		calculator.set_word("DWord");
		Assert.assertEquals(calculator.display(), "-420990904");


	}
	@Test
	void test_add(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator.add("10", "5");
		Assert.assertEquals(calculator.display(), "15");

		calculator.add("3", "4");
		Assert.assertEquals(calculator.display(), "7");

		calculator.add("10", "5");
		Assert.assertNotEquals(calculator.display(), "13");

		calculator.add("3", "4");
		Assert.assertNotEquals(calculator.display(), "2");
	}
	@Test
	void test_sub(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator.sub("10", "5");
		Assert.assertEquals(calculator.display(), "5");

		calculator.sub("3", "4");
		Assert.assertEquals(calculator.display(), "-1");

		calculator.sub("10", "5");
		Assert.assertNotEquals(calculator.display(), "13");

		calculator.sub("3", "4");
		Assert.assertNotEquals(calculator.display(), "2");
	}
	@Test
	void test_mul(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator.mul("10", "5");
		Assert.assertEquals(calculator.display(), "50");

		calculator.mul("3", "4");
		Assert.assertEquals(calculator.display(), "12");

		calculator.mul("10", "5");
		Assert.assertNotEquals(calculator.display(), "13");

		calculator.mul("3", "4");
		Assert.assertNotEquals(calculator.display(), "2");
	}
	@Test
	void test_div(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator.div("10", "5");
		Assert.assertEquals(calculator.display(), "2");

		calculator.div("4", "4");
		Assert.assertEquals(calculator.display(), "1");

		calculator.div("10", "5");
		Assert.assertNotEquals(calculator.display(), "13");

		calculator.div("3", "4");
		Assert.assertNotEquals(calculator.display(), "2");
	}
	@Test
	void test_neg(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator._neg("10");
		Assert.assertEquals(calculator.display(), "-10");

		calculator._neg("4");
		Assert.assertEquals(calculator.display(), "-4");

		calculator._neg("10");
		Assert.assertNotEquals(calculator.display(), "13");

		calculator._neg("4");
		Assert.assertNotEquals(calculator.display(), "2");
	}
	@Test
	void test_and(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator._and("10", "5");
		Assert.assertEquals(calculator.display(), "0");

		calculator._and("12", "8");
		Assert.assertEquals(calculator.display(), "8");

		calculator._and("10", "5");
		Assert.assertNotEquals(calculator.display(), "2");

		calculator._and("12", "8");
		Assert.assertNotEquals(calculator.display(), "3");
	}
	@Test
	void test_or(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator._or("10", "5");
		Assert.assertEquals(calculator.display(), "15");

		calculator._or("12", "8");
		Assert.assertEquals(calculator.display(), "12");

		calculator._or("10", "5");
		Assert.assertNotEquals(calculator.display(), "4");

		calculator._or("12", "8");
		Assert.assertNotEquals(calculator.display(), "32");
	}
	@Test
	void test_xor(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator._xor("10", "5");
		Assert.assertEquals(calculator.display(), "15");

		calculator._xor("12", "8");
		Assert.assertEquals(calculator.display(), "4");

		calculator._xor("10", "5");
		Assert.assertNotEquals(calculator.display(), "3");

		calculator._xor("12", "8");
		Assert.assertNotEquals(calculator.display(), "12");
	}
	@Test
	void test_not(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator._not("10");
		Assert.assertEquals(calculator.display(), "-11");

		calculator._not("12");
		Assert.assertEquals(calculator.display(), "-13");

		calculator._not("10");
		Assert.assertNotEquals(calculator.display(), "15");

		calculator._not("4");
		Assert.assertNotEquals(calculator.display(), "-133");
	}
	@Test
	void test_rol(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator._rol("10");
		Assert.assertEquals(calculator.display(), "20");

		calculator._rol("12");
		Assert.assertEquals(calculator.display(), "24");

		calculator._rol("10");
		Assert.assertNotEquals(calculator.display(), "23");

		calculator._rol("12");
		Assert.assertNotEquals(calculator.display(), "2");
	}
	@Test
	void test_ror(){
		Calculator calculator = new Calculator(10, "QWord");
		
		calculator._ror("10");
		Assert.assertEquals(calculator.display(), "5");

		calculator._ror("12");
		Assert.assertEquals(calculator.display(), "6");

		calculator._ror("10");
		Assert.assertNotEquals(calculator.display(), "23");

		calculator._ror("12");
		Assert.assertNotEquals(calculator.display(), "2");
	}

}
