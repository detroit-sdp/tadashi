#!/usr/bin/env python
import sys
import serial
import time
#from std_msgs.msg import ByteMultiArray



def reconnect(): 
    while (ser.inWaiting() == 0): 
        ser.write(b'\x00')
        print("reconnecting")
        time.sleep(0.05)
    time.sleep(1)
    in_size = ser.inWaiting()
    if (in_size > 0): ser.read(in_size - 2)
    
    
    
    
ser = serial.Serial('/dev/ttyACM0',115200)
inBytes = b'\x00\x00'
#outByte = bytes(chr(int(sys.argv[1])), encoding = 'utf-8')
outByte = "\x01"
waiting = False
event = 0.0
while True:
    status  = []
    ser.write(outByte)
    i = 0
    #print("Before loop")
    while (ser.inWaiting() == 0): 
        time.sleep(0.05)
        #print(i)
        if (i == 20): 
            reconnect()
            break
        else: 
            i = i + 1    
    inBytes = ser.read(2)
    
    # arduino_data = ByteMultiArray()
    #arduino_data.data = inBytes
    #rospy.init_node('serial_test_node')
    #arduino_pub = rospy.Publisher('arduino_data', ByteMultiArray, queue_size=10)
    #arduino_pub.publish(arduino_data)
    if ((int(ord(inBytes[1])) >> 0) % 2 == 1): status.append("extending")
    if ((int(ord(inBytes[1])) >> 1) % 2 == 1): status.append("extended")
    if ((int(ord(inBytes[1])) >> 2) % 2 == 1): status.append("retracting")
    if ((int(ord(inBytes[1])) >> 3) % 2 == 1): status.append("retracted")
    print("weight: " + str(int(ord(inBytes[0]))) + '\t' + 
            "status: " + str(status))    
    if(not(waiting) & ((int(ord(inBytes[1])) == 2) | (int(ord(inBytes[1])) == 8))): 
        waiting = True
        event = time.time()
    if (waiting & ((time.time() - event)  > 3.0)): 
        waiting = False
        outByte = bytes(chr(ord(outByte) ^ 3).encode('utf-8'))


