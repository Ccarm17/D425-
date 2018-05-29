
"""
File: skidsteer_four_pwm_test.py

This code will test Raspberry Pi GPIO PWM on four GPIO
pins. The code test ran with L298N H-Bridge driver module connected.

Website:	www.bluetin.io
Date:		27/11/2017
"""

__author__ = "Mark Heywood"
__version__ = "0.1.0"
__license__ = "MIT"

import curses
from gpiozero import PWMOutputDevice, Button
from time import sleep
from subprocess import check_call




#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS

PWM_FORWARD_LEFT_PIN = 26	# IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 19	# IN2 - Reverse Drive

# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 13	# IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 6	# IN2 - Reverse Drive

# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 500)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 500)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 500)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 500)

leftBump = Button(21)
rightBump = Button(20)

# Motor A, Trim % of difference

# Motor B, Trim % of difference


# speed = Battery voltage ^-1 x motor speed
def allStop():
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0

def forwardDrive():
        forwardLeft.value = 0.2
        reverseLeft.value = 0
        forwardRight.value = 0.2
        reverseRight.value = 0

def reverseDrive():
	forwardLeft.value = 0
	reverseLeft.value = 0.15
	forwardRight.value = 0
	reverseRight.value = 0.15

def spinLeft():
	forwardLeft.value = 0
	reverseLeft.value = 0.15
	forwardRight.value = 0.15
	reverseRight.value = 0

def spinRight():
	forwardLeft.value = 0.15
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0.15

def leftBumpOn():
	forwardLeft.value = 0.2
	reverseLeft.value = 0
	forwardRight.value = 0.8
	reverseRight.value = 0

def rightBumpOn():
	forwardLeft.value = 0.8
	reverseLeft.value = 0
	forwardRight.value = 0.2
	reverseRight.value = 0
	print('right bump')
	sleep(0.5)




def main():
        while True:
         char= raw_input()


         if char =='q':
             break
         elif char =='s':
                 forwardDrive()
         elif char =='w':
                 reverseDrive()
         elif char == 'd':
                 spinLeft()
         elif char == 'a':
                 spinRight()
         elif char == 'f':
                 allStop()
         rightBump.when_pressed = rightBumpOn
 

        



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
