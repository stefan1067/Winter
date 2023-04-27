import machine
from machine import Pin
import time
from machine import I2C

#from smbus import SMBus
#prova
#
# Setup
green = Pin("PC5", Pin.OUT)
red = Pin("PB0", Pin.OUT)

i2c = machine.I2C(scl=machine.Pin("PB6"), sda=machine.Pin("PB7"))   #inizializzazione accesso a I2C
i2c .scan ()	#Scansione della scheda
#adress=indirizzo dispositivo i2c della scheda
#barometro=indirizzo memoria registro da leggere dal dispositivo
#nbyte=numero di byte da leggere
data = bytearray(2)
#i2c.readfrom_mem_into(address, PB7, data)
#La funzione readfrom_mem restituirà una stringa di byte con i dati recuperati dal dispositivo e successivamente esecuzionde del print

# Loop
while True:
	print("prova")
	green.value(1)
	red.value(0)
	green.value(1)
	time.sleep(1)
	green.value(0)
	red.value(1)
	time.sleep(1)
