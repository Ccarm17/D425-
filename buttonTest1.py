from gpiozero import Button
from signal import pause
from subprocess import check_call

button = Button(17)

button1 = Button(27)

button2 = Button(22)

def shutdown():
    check_call(['sudo', 'poweroff'])
    
def buttonDown():
    print('Down')
    
def buttonUp():
    print('Up')
    
def buttonDown1():
    print('Down1')
    
def buttonUp1():
    print('Up1')
    
button.when_pressed = buttonDown
button.when_released = buttonUp

button1.when_pressed = buttonDown1
button1.when_released = buttonUp1

button2.when_pressed = shutdown
pause()
