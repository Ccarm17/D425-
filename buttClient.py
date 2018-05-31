import socket
from time import sleep
from gpiozero import Button
from signal import pause
from subprocess import check_call

host = '192.168.1.102'
port = 5560


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def Shutdown():
    check_call(['sudo', 'poweroff'])

def forwardButton():
    print('forward')
    s.send(str.encode('FORWARD'))

def backwardButton():
    print('back')
    s.send(str.encode('BACKWARD'))

def leftButton():
    print('left')
    s.send(str.encode('LEFT'))

def rightButton():
    print('right')
    s.send(str.encode('RIGHT'))

def stopButton():
    print('FUCK')
    s.send(str.encode('STOP'))



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
pause()
