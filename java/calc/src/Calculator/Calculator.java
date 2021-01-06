package Calculator;

public class Calculator {
	int system;
	String word;
	String current_value;
	
	public Calculator(int system, String word){
		this.system = system;
		this.word = word;
		this.current_value = "";
	}
	
	public void set_system(int system) {
		if (this.current_value != "") {
			this.current_value = convert_system(this.current_value, this.system, system);
		}
		this.system = system;
	}
	
	public void set_word(String word) {
		this.word = word;
	}
	
	public void clear() {
		this.current_value = "";
	}
	
	public String convert_system(String value, int input_system, int output_system) {
		if (input_system == output_system) {
			return value;
		}
		int dec = Integer.parseInt(value, input_system); 
		if (output_system == 10) {
			return String.valueOf(dec);
		}
		else if (output_system == 8) {
			return Integer.toOctalString(dec);
		}
		else if (output_system == 16) {
			return Integer.toHexString(dec);
		}
		else if (output_system == 2) {
			return Integer.toBinaryString(dec);
		}
		return "false";
	}
	
	public boolean check_value_system(String value, int system) {
		char [] allowed_chars = {'-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
		value = value.toUpperCase();
		int result = 0;
		for(int i=0; i<value.length();i++) {
			for(int j=0; j<system+1;j++) {
				if(value.charAt(i)==allowed_chars[j]) {
					result += 1;
				}
			}
		}
		if (result == value.length()) {
			return true;
		}
		return false;
	}
	
	
	public boolean check_value_word(String value) {
		int tmp = Integer.parseInt(convert_system(value, this.system, 10));
		if (this.word == "Byte" && -128 <= tmp && tmp <=128) {
			return true;
		}
		else if (this.word == "Word" && -32768 <= tmp && tmp <=32676) {
			return true;
		}
		else if (this.word == "DWord" && -2147450880 <= tmp && tmp <=2147450879) {
			return true;
		}
		else if (this.word == "QWord" && Long.parseLong("-9223372036854775808") <= tmp && tmp <= Long.parseLong("9223372036854775807")) {
			return true;
		}
		return false;
	}
	
	
	public String display() {
		System.out.println(this.current_value);
		return this.current_value;
	}
	
	public void insert_whole_value(String value) {
		if(check_value_system(value, this.system) && check_value_word(value)) {
			this.current_value = value;
		}
	}
	
	public void insert_step_value(String step) {
		String tmp = this.current_value + step;
		if(check_value_system(tmp, this.system) && check_value_word(tmp)) {
			this.current_value = tmp;
		}
	}	
	
	public void add(String a, String b) {
		String c = String.valueOf(Integer.parseInt(a)+Integer.parseInt(b));
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}
	
	public void sub(String a, String b) {
		String c = String.valueOf(Integer.parseInt(a)-Integer.parseInt(b));
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}	
	
	public void mul(String a, String b) {
		String c = String.valueOf(Integer.parseInt(a)*Integer.parseInt(b));
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}	
	
	public void div(String a, String b) {
		String c = String.valueOf(Integer.parseInt(a)/Integer.parseInt(b));
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}	
	
	public void neg(String a) {
		String c = String.valueOf(~Integer.parseInt(a)+1);
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}	
	
	public void and(String a, String b) {
		String c = String.valueOf(Integer.parseInt(a)&Integer.parseInt(b));
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}		
	
	public void or(String a, String b) {
		String c = String.valueOf(Integer.parseInt(a)|Integer.parseInt(b));
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}	
	
	public void xor(String a, String b) {
		String c = String.valueOf(Integer.parseInt(a)^Integer.parseInt(b));
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}	
	
	public void not(String a) {
		String c = String.valueOf(~Integer.parseInt(a));
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}	

	public void rol(String a) {
		String c = String.valueOf(Integer.parseInt(a)<<1);
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}	
	
	
	public void ror(String a) {
		String c = String.valueOf(Integer.parseInt(a)>>1);
		if(check_value_system(c, this.system) && check_value_word(c)) {
			this.current_value = c;
		}
	}	
		
	
	
	
	
	public static void main(String[] args) {

		Calculator calc = new Calculator(10, "Word");	

		System.out.println(calc.convert_system("10", 10, 2));
		System.out.println(calc.convert_system("-10", 10, 2));
		
		System.out.println(calc.check_value_system("-77fg", 16));
		System.out.println(calc.check_value_system("89", 16));
		
		calc.insert_whole_value("129");
		calc.display();
		
		calc.clear();
		calc.set_system(10);
		calc.set_word("Word");
		calc.insert_step_value("1");
		calc.display();
		calc.insert_step_value("2");
		calc.display();
		calc.insert_step_value("9");
		calc.display();
		
	}
}