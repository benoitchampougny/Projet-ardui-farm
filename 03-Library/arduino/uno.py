# -*-coding: utf-8 -*

#####################################################################################################
#                       TITLE
#####################################################################################################

brand="arduino"
model="uno"

#####################################################################################################
#                       ACCOUNT PIN
#####################################################################################################

number_of_pin_digital_IO = 14
number_of_pin_analog_INPUT = 6

#####################################################################################################
#                       DETAIL PIN
#####################################################################################################

detail_of_pin_digital_IO = []
for a in range(number_of_pin_digital_IO):
    detail_of_pin_digital_IO.append([])

detail_of_pin_digital_IO [0]= ["rx"]
detail_of_pin_digital_IO [1]= ["tx"]
detail_of_pin_digital_IO [2]= [""]
detail_of_pin_digital_IO [3]= ["pwm"]
detail_of_pin_digital_IO [4]= [""]
detail_of_pin_digital_IO [5]= ["pwm"]
detail_of_pin_digital_IO [6]= ["pwm"]
detail_of_pin_digital_IO [7]= [""]
detail_of_pin_digital_IO [8]= [""]
detail_of_pin_digital_IO [9]= ["pwm"]
detail_of_pin_digital_IO [10]= ["pwm","ss"]
detail_of_pin_digital_IO [11]= ["pwm","mosi"]
detail_of_pin_digital_IO [12]= ["miso"]
detail_of_pin_digital_IO [13]= ["sck"]


detail_of_pin_analog_INPUT = []
for a in range(number_of_pin_digital_IO):
    detail_of_pin_analog_INPUT.append([])

detail_of_pin_analog_INPUT [0]= [""]
detail_of_pin_analog_INPUT [1]= [""]
detail_of_pin_analog_INPUT [2]= [""]
detail_of_pin_analog_INPUT [3]= [""]
detail_of_pin_analog_INPUT [4]= ["sda"]
detail_of_pin_analog_INPUT [5]= ["scl"]

print (detail_of_pin_analog_INPUT_IO [5])


