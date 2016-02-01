# -*- coding: utf8 -*-

#**************************************************************************<< make sketch >>**********************************************************************************************************
def make_void_setup( number_digital_pin, number_analog_pin, list_PWM_pin, list_I2C_pin, list_setup_pin_digital_INPUT, list_setup_pin_digital_OUTPUT,  list_setup_pin_analog, list_setup_pin_PWM, adress_I2C):
	
	number_digital_pin_setup = len(list_setup_pin_digital_INPUT) + len(list_setup_pin_digital_OUTPUT)
	number_analog_pin_setup = len(list_setup_pin_analog)
	number_PWM_pin_setup = len(list_setup_pin_PWM)
	
	result_error = ""
	compatibility = False
	
	list_digital_pin_used = []
	list_analog_pin_used = []
	list_PWM_pin_used = []
	
	if list_I2C_pin [0][0] == "A":
		number_analog_pin_setup = number_analog_pin_setup -2
		list_analog_pin_used = list_I2C_pin
	else:
		list_digital_pin_used = list_I2C_pin
		number_digital_pin_setup = number_digital_pin_setup -2
		for a in range (len(list_PWM_pin)):
			for b in range (len(list_I2C_pin)):
				if list_PWM_pin [a] == list_I2C_pin [b] :
					list_PWM_pin_used = list_I2C_pin
					list_digital_pin_used = []
					number_digital_pin_setup = number_digital_pin_setup +2
					number_PWM_pin_setup = number_PWM_pin_setup -2
	
	if number_PWM_pin_setup > len(list_PWM_pin):
		result_error = "error pwm number"
	if number_digital_pin_setup > number_digital_pin :
		result_error = "error digital number"
	if number_analog_pin_setup > number_analog_pin :
		result_error = "error analog number"
	for a in range (len(list_PWM_pin)) :
		for b in range (len(list_setup_pin_PWM)) :
			if compatibility == False :
				if list_PWM_pin [a] == list_setup_pin_PWM [b] :
					compatibility = True
		if compatibility == False :
			result_error = "error compatibility pwm"
	
	if result_error == "" :
		result = "void setup() { \n\tSerial.begin(9600);\n\tWire.begin(" + str(adress_I2C) + ");\n\tWire.onReceive(receiveEvent);\n\t"
		for a in range (len(list_setup_pin_PWM)) :
			conflict = False
			for b in range (len(list_PWM_pin_used)) :
				if list_setup_pin_PWM [a] == list_PWM_pin_used [b] :
					conflict = True
					result_error = "error conflitct pwm"
			if conflict == False :
				list_PWM_pin_used.append(list_setup_pin_PWM[a])
				result = result + "pinMode(" + str(list_setup_pin_PWM[a]) + ", output); // analog output (PWM)\n\t"
		
		list_digital_pin_used = list_digital_pin_used + list_PWM_pin_used
		for a in range (len(list_setup_pin_digital_INPUT)) :
			conflict = False
			for b in range (len(list_digital_pin_used)) :
				if list_setup_pin_digital_INPUT [a] == list_digital_pin_used [b] :
					conflict = True
					result_error = "error double digital pin"
			if conflict == False :
				list_digital_pin_used.append(list_setup_pin_digital_INPUT[a])
				result = result + "pinMode(" + str(list_setup_pin_digital_INPUT[a]) + ", input); // digital input\n\t"	
		
		
		for a in range (len(list_setup_pin_digital_INPUT)) :
			conflict = False
			for b in range (len(list_digital_pin_used)) :
				if list_setup_pin_digital_OUTPUT [a] == list_digital_pin_used [b]:
					conflict = True
					result_error = "error double digital pin"
			if conflict == False :
				list_digital_pin_used.append(list_setup_pin_digital_OUTPUT[a])
				result = result + "pinMode(" + str(list_setup_pin_digital_OUTPUT[a]) + ", output); // digital output\n\t"
		
		for a in range (len(list_setup_pin_analog)):
			conflict = False
			for b in range (len(list_analog_pin_used)) :
				if list_setup_pin_analog [a] == list_analog_pin_used [b] :
					conflict = True
					result_error = "error double analog pin"
			if conflict == False :
				list_analog_pin_used.append(list_setup_pin_analog[a])
				result = result + "// analog input" + str(list_setup_pin_analog[a]) + "\n\t"			
		result = result + "}"
	if result_error == "" :	
		final_result = result
	else: 
		final_result = result_error
	return final_result
	
"""test
number_digital_pin = 14
number_analog_pin = 6 	
list_PWM_pin = [11,10,9,6,5,3]
list_I2C_pin = ["A4","A5"]

list_setup_pin_digital_INPUT= [3,7]
list_setup_pin_digital_OUTPUT= [5,13]
list_setup_pin_analog = ["A0","A1"]
list_setup_pin_PWM= [11,6]

adress_I2C= 8

test = make_void_setup( number_digital_pin, number_analog_pin, list_PWM_pin, list_I2C_pin, list_setup_pin_digital_INPUT, list_setup_pin_digital_OUTPUT,  list_setup_pin_analog, list_setup_pin_PWM, adress_I2C)

print(test)

"""

def make_void_loop(
