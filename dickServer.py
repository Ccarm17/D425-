import socket
from gpiozero import PWMOutputDevice, Button
from time import sleep
from subprocess import check_call

#running on D425 droid
host = ''
port = 5560

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

speedmod = 1
turnmod = 1

rightBump.when_pressed = rightBumpOn()
leftBump.when_pressed = leftBumpOn()

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def allStop():
	forwardLeft.value = 0
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0

def forwardDrive():
    forwardLeft.value = 0.2 * speedmod
    reverseLeft.value = 0
    forwardRight.value = 0.2 * speedmod
	reverseRight.value = 0

def reverseDrive():
	forwardLeft.value = 0
	reverseLeft.value = 0.15 * speedmod
	forwardRight.value = 0
	reverseRight.value = 0.15 * speedmod

def spinLeft():
	forwardLeft.value = 0
	reverseLeft.value = 0.15 * turnmod
	forwardRight.value = 0.15 * turnmod
	reverseRight.value = 0

def spinRight():
	forwardLeft.value = 0.15 * trunmod
	reverseLeft.value = 0
	forwardRight.value = 0
	reverseRight.value = 0.15 * turnmod

def leftBumpOn():
	forwardLeft.value = 0.2
	reverseLeft.value = 0
	forwardRight.value = 0.8
	reverseRight.value = 0
	print('left bump')
	sleep(0.2)
	return

def rightBumpOn():
	forwardLeft.value = 0.8
	reverseLeft.value = 0
	forwardRight.value = 0.2
	reverseRight.value = 0
	print('right bump')
	sleep(0.5)
	return None

def switch1aOn():

def switch1bOn():

def switch2On():

def switch3On():

def switch4On():

def switch5On():

def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]

        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Our client has left us :(")
            break
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
            break
        elif command == 'FORWARD':
            print('forward')
            reply = forwardDrive()
        elif command == 'BACKWARD':
            print ('backward')
            reply = reverseDrive()
        elif command == 'LEFT':
            print('left')
            reply = spinLeft()
        elif command == 'RIGHT':
            print('right')
            reply = spinRight()
        elif command == 'STOP':
            print('stop')
            reply = allStop()

        elif command == 'S1AOn':
            print('switch 1 A has been activated')
            reply = switch1aOn()

        elif command == 'S1BOn':
            print('switch 1 B has been activated')
            reply = switch1bOn()

        elif command == 'S2On':
            print('switch 2 has been activated')
            reply = switch2On()

        else:
            reply = 'Unknown Command'
        # Send the reply back to the client
        #conn.sendall(str.encode(reply))

        #print("Data has been sent!")



    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break
