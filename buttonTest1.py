import curses
import socket
import keyboard
from gpiozero import Button
from signal import pause
from subprocess import check_call

forward = Button(17)

backward = Button(27)

left = Button(22)

right = Button()

shutdown = Button()

def shutdown():
    check_call(['sudo', 'poweroff'])

def forwardButton():
    keyboard.write

def backwardButton():
    print('Up')

def leftButton():
    print('Down1')

def rightButton():
    print('Up1')

button.when_pressed = buttonDown
button.when_released = buttonUp

button1.when_pressed = buttonDown1
button1.when_released = buttonUp1

button2.when_pressed = shutdown
pause()
