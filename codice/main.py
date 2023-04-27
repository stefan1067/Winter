from machine import Pin
import time
from smbus import SMBus
#import smbus
# Setup
green = Pin("PC5", Pin.OUT)
red = Pin("PB0", Pin.OUT)

i2cbus = SMBus(1) #creo un nuovo collegamento i2c
sda = Pin("PB7",Pin.OUT)	#serial data
scl=Pin("PB6",Pin.OUT)	#serial clock

#adress device
# Loop
while True:
	#portb = i2cbus.read_byte_data(adress device, sda)  # Read the value of Port sda
	#print(sda)
	red.value(0)
	green.value(1)
	time.sleep(1)
	green.value(0)
	red.value(1)
	time.sleep(1)

#prova con libreria SMBus2
#from smbus2 import SMBus

# Open i2c bus 1 and read one byte from address 80, offset 0
#bus = SMBus(1)
#b = bus.read_byte_data(80, 0)
#print(b)
#bus.close()
