import serial

# ser = serial.Serial(port='[TBC]', baudrate=9600, bytesize=8, timeout=0.1)
# TODO: change port

while True:
	# arduino_status = ser.read(size=1)	# number of bytes to read
	# print(arduino_status)
	status = b'\x01'
	# ser.write(status)
	print(status)