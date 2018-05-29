from gpiozero import Button
from signal import pause
from subprocess import check_call


def Shutdown():
    check_call(['sudo', 'poweroff'])

def forwardButton():
    print('forward')
    

def backwardButton():
    print('back')

def leftButton():
    print('left')

def rightButton():
    print('right')

def stopButton():
    print('FUCK')

forward = Button(21)

backward = Button(20)

left = Button(22)

right = Button(4)

shutdown = Button(16)
    

forward.when_pressed = forwardButton
forward.when_released = stopButton

backward.when_pressed = backwardButton
backward.when_released = stopButton

left.when_pressed = leftButton
left.when_released = stopButton

right.when_pressed = rightButton
right.when_released = stopButton

shutdown.when_pressed = Shutdown
print('end')
pause()
