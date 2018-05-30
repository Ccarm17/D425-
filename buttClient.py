import socket
from time import sleep
from gpiozero import Button
from signal import pause
from subprocess import check_call

host = '192.168.1.79'
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

def switch1aOn():
    print('S1AOn')
    s.send(str.encode('S1AOn'))

def switch1bOn():
    print('S1BOn')
    s.send(str.encode('S1BOn'))

def switch2On():
    print('S2On')
    s.send(str.encode('S2On'))

def switch3On():
    print('S3On')
    s.send(str.encode('S3On'))

def switch4On():
    print('S4On')
    s.send(str.encode('S4On'))

def switch5On():
    print('S5On')
    s.send(str.encode('S5On'))

def switch1aOff():
    print('S1AOn')
    s.send(str.encode('S1AOff'))

def switch1bOff():
    print('S1BOff')
    s.send(str.encode('S1BOff'))

def switch2Off():
    print('S2Off')
    s.send(str.encode('S2Off'))

def switch3Off():
    print('S3Off')
    s.send(str.encode('S3Off'))

def switch4Off():
    print('S4Off')
    s.send(str.encode('S4Off'))

def switch5Off():
    print('S5Off')
    s.send(str.encode('S5Off'))

forward = Button(21)

backward = Button(20)

left = Button(22)

right = Button(4)

shutdown = Button(16)

switch1a = Button(26)
switch1b = Button(19)
switch2 = Button(13)
switch3 = Button(6)
switch4 = Button(5)
Switch5 = Button(21)

forward.when_pressed = forwardButton
forward.when_released = stopButton

backward.when_pressed = backwardButton
backward.when_released = stopButton

left.when_pressed = leftButton
left.when_released = stopButton

right.when_pressed = rightButton
right.when_released = stopButton

switch1a.when_pressed = switch1aOn
switch1b.when_pressed = switch1bOn
switch2.when_pressed = switch2On
switch3.when_pressed = switch3On
switch4.when_pressed = switch4On
switch5.when_pressed = switch5On

switch1a.when_released = switch1aOff
switch1b.when_released = switch1bOff
switch2.when_released = switch2Off
switch3.when_released = switch3Off
switch4.when_released = switch4Off
switch5.when_released = switch5Off

shutdown.when_pressed = Shutdown
pause()
